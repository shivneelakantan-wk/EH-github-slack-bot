from dotenv import load_dotenv
import os
from github import Github
from github.Auth import Token


def get_open_pull_requests(repo_owner, repo_name):
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

        event_horizon_prs = []

        for pr in open_prs:
            x = pr.user.login
            print(x)

    except:
        pass

if __name__ == '__main__':
    get_open_pull_requests('shivneelakantan-wk', 'EH-github-slack-bot')