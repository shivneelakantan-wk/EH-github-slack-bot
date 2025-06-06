# 🚧 Github Slack Bot Pro 🚧

### Sample Message
```
Good morning! Here are the outstanding PRs for the [team name] team:

Repo 1
- PR 1, authored by author 1 (link), needs code review and QA review
- PR 2, authored by author 2 (link), needs QA review

Repo 2
- PR 3, authored by author 1 (link), needs security review

Repo 3
- PR 4, authored by author 3 (link), needs QA review and security review
```

### Motivation

The purpose of this integration is to send an aggregated list of all open Github PRs a team owns on a fixed schedule to a team's slack channel. 

While there is already an existing [Github integration provided in our Slack workspaces](https://workiva.slack.com/marketplace/A01BP7R4KNY-github?settings=1&tab=settings) that lets us subscribe to a repository and receive all of its open PRs, this tool has the following limitations:
1. The existing integration only fetches PRs for a single repo at a time. For teams that work in multiple different repositories (such as the [Event Horizon team](https://wiki.atl.workiva.net/spaces/SOXDEV/pages/430704955/Event+Horizon), which contributes to nearly 10 repos across frontend, backend, and frugal), it can be noisy to receive a separate message for each repository. 
2. The existing tool fetches **all** open PRs, including ones that are not created by the team (or channel members). This can furthermore exacerbate the noisiness if the repository is shared with other teams.
3. The existing tool does not let us customize specifically which types of PRs we need, or inform us on which reviews are outstanding. 

### Solution

The integration defined in this repository seeks to solve these limitations by extending the existing Github bot's functionality. When onboarding this bot into a specific channel, users will be able to specify the following criteria to filter PRs:
- Repository names
- List of team members
- Reviews outstanding (code review, QA review, security review if necessary)

With this setup, teams can customize the message they receive to contain all of the repositories they own, filtered by only PRs that their team has authored, as well as a minimum PR age (i.e. 2 days). This improved view would allow teams to effectively visualize what outstanding work needs what review types on a daily basis, reducing both review turnaround and the need to manually call out stale PRs. 

### Architecture
TODO

### Limitations
- Waiting on approval from Workiva's slack admin team
