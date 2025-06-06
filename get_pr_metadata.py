from dotenv import load_dotenv
import os
from github import Github
from github.Auth import Token

class PR_DTO:
    def __init__(self, pr_title, pr_author_username, pr_url, pr_date):
        self.pr_title = pr_title
        self.pr_author_username = pr_author_username
        self.pr_url = pr_url
        self.pr_date = pr_date

def get_open_pull_requests_for_repo(repo_owner, repo_name, team_member_usernames):
    '''
    fetches and returns details of all open PRs for a given github repo.
    :param repo_owner:
    :param repo_name:
    :return:
    '''
    load_dotenv()
    github_token = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')

    if not github_token:
        print('ERROR: could not find github pat or could not find .env file')

    try:
        # authenticate with github using token
        auth = Token(github_token)
        g = Github(auth=auth)

        # get the repo
        user = g.get_user(repo_owner) if repo_owner else g.get_user()
        repository = user.get_repo(repo_name)
        print(f'fetching open PRs for {repo_owner}/{repo_name}...')

        # get all open PRs
        open_prs = repository.get_pulls(state='open')

        teams_prs = []

        for pr in open_prs:
            pr_title = pr.title
            pr_author_username = pr.user.login

            if pr_author_username not in team_member_usernames:
                continue

            pr_id = pr.url.split('/')[-1]
            pr_url = f'https://github.com/{repo_owner}/{repo_name}/pull/{pr_id}'
            pr_date = pr.created_at.strftime('%Y-%m-%d %H:%M:%S')

            pr_object = PR_DTO(pr_title, pr_author_username, pr_url, pr_date)
            teams_prs.append(pr_object)

        return teams_prs

    except:
        pass


def get_open_pull_requests_for_list_of_repos(repo_owner, repo_names, team_member_usernames):
    '''
    fetches and returns details of all open PRs for a list of github repos.
    :param team_member_usernames:
    :param repo_owner:
    :param repo_names:
    :return:
    '''
    event_horizon_prs = []
    for repo_name in repo_names:
        prs = get_open_pull_requests_for_repo(repo_owner, repo_name, team_member_usernames)
        if prs:
            event_horizon_prs.extend(prs)

    return event_horizon_prs

if __name__ == '__main__':
    get_open_pull_requests_for_list_of_repos('shivneelakantan-wk',
                                             ['EH-github-slack-bot'],
                                             set('shivneelakantan-wk')
                                             )