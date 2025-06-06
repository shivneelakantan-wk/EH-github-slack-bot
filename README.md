Github bot to notify teams via slack all outstanding PRs made by their team across all relevant repositories.

# 🚧 Github Slack Bot Pro 🚧

### Motivation

The purpose of this integration is to send an aggregated list of all open Github PRs a team owns on a fixed schedule (i.e., daily at 9am CST). 

While there is already an existing Github integration provided in our Slack workspaces that lets us subscribe to a repository and receive all of its open PRs, this tool can have limitations when being used by teams with multiple different repositories they would like to keep track of (such as the [Event Horizon team](https://wiki.atl.workiva.net/spaces/SOXDEV/pages/430704955/Event+Horizon)), as we would need to manage an independent tracker for each repository. Furthermore, the existing tool fetches all open PRs, including ones that are not created by the team (or channel members). This can make the message very noisy if the repository is shared with other teams, or has outstanding stale PRs. 

### Solution

The integration defined in this repository seeks to solve this limitation by extending the existing Github bot's functionality. When onboarding this bot into a specific channel, users will be able to specify the following criteria to filter PRs:
- Repository name
- List of team members
- Number of outstanding days

This setup allows teams to customize the message they receive to contain all of the repositories they own, filtered by only PRs that their team has authored as well as a minimum PR age (i.e. 2 days). This improved view would allow teams to effectively visualize what outstanding work needs review on a daily basis, reducing both review turnaround and the need to manually call out stale PRs. 

### Architecture
TODO

### Limitations
- Waiting on approval from Workiva's slack admin team
