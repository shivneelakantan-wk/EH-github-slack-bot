import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from get_pr_metadata import PR_DTO, _get_open_pull_requests_for_repo, get_open_pull_requests_for_list_of_repos


def send_slack_message(channel_id, message_text, client):
    try:
        response = client.chat_postMessage(
            channel=channel_id,
            text=message_text
        )

        print(f"Message sent successfully to channel {channel_id}: {response['message']['text']}")
        return True

    except SlackApiError as e:
        print(f"Error sending message to channel {channel_id}: {e.response['error']}")
        return False

def format_prs_for_slack(pr_dto_list, repo_owner, repo_name):
    """
    Formats a list of PR DTOs into a Slack message.
    :param pr_dto_list: List of PR DTOs
    :param repo_owner: Owner of the repository
    :param repo_name: Name of the repository
    :return: Formatted message string
    """
    if not pr_dto_list:
        return f"No open PRs found for {repo_owner}/{repo_name}."

    message_lines = [f"Open PRs for *{repo_owner}/{repo_name}*:\n"]

    for pr in pr_dto_list:
        message_lines.append(f"- *{pr.title}* by @{pr.author_username} - <{pr.url}|View PR> (Created on {pr.date})")

    return "\n".join(message_lines)

if __name__ == '__main__':
    load_dotenv()
    slack_bot_token = os.getenv('SLACK_BOT_TOKEN')
    slack_channel_id = os.getenv('SLACK_CHANNEL_ID')

    if not slack_bot_token:
        print("Error: SLACK_BOT_TOKEN not found in environment variables.")
        exit(1)

    client = WebClient(token=slack_bot_token)

    message_text = "Hello, Slack!"

    if send_slack_message(slack_channel_id, message_text, client):
        print("Message sent successfully.")
    else:
        print("Failed to send message.")