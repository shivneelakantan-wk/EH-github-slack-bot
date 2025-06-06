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


def _get_open_pull_requests_for_repo(repo_owner, repo_name, team_member_usernames):
    '''
    fetches and returns details of all open PRs for a given github repo.
    :param repo_owner:
    :param repo_name:
    :return:
    '''
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

        teams_prs_for_repo = []

        for pr in open_prs:
            pr_title = pr.title
            pr_author_username = pr.user.login

            if pr_author_username.strip() not in team_member_usernames:
                continue

            pr_id = pr.url.split('/')[-1]
            pr_url = pr.html_url
            pr_date = pr.created_at.strftime('%Y-%m-%d %H:%M:%S')

            pr_object = PR_DTO(pr_title, pr_author_username, pr_url, pr_date)
            teams_prs_for_repo.append(pr_object)

        return teams_prs_for_repo

    except Exception as e:
        print(f'ERROR: could not fetch open PRs for {repo_owner}/{repo_name} - {e}')


def get_open_pull_requests_for_list_of_repos(repo_owner, repo_names, team_member_usernames):
    '''
    fetches and returns details of all open PRs for a list of github repos.
    :param team_member_usernames:
    :param repo_owner:
    :param repo_names:
    :return:
    '''
    teams_prs = []
    for repo_name in repo_names:
        prs = _get_open_pull_requests_for_repo(repo_owner, repo_name, team_member_usernames)
        if prs:
            teams_prs.extend(prs)
    print(f'found {len(teams_prs)} open PRs for {repo_owner} in repos {repo_names}')
    return teams_prs

def send_slack_message(channel_id, message_text, client):
    '''
    Sends a message to a Slack channel.
    :param channel_id: ID of the Slack channel
    :param message_text: Text of the message to send
    :param client: Slack client instance
    '''
    try:
        response = client.chat_postMessage(channel=channel_id, text=message_text)
        print(f'Message sent successfully: {response["ts"]}')
    except Exception as e:
        print(f'Error sending message: {e}')


if __name__ == '__main__':
    load_dotenv()
    prs = get_open_pull_requests_for_list_of_repos('shivneelakantan-wk',
                                                   ['EH-github-slack-bot'],
                                                   {'shivneelakantan-wk'}
                                                   )
    for pr in prs:
        print(f'Title: {pr.pr_title}, Author: {pr.pr_author_username}, URL: {pr.pr_url}, Date: {pr.pr_date}')
