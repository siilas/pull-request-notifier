# Pull Request Notifier

*A simple service that sends slack notifications if a pull request still open after X days.*

## What it really does?

It gets the opened pull requests from a GitHub repository and send a Slack notification to a channel. But just if the pull request still open after a predefined number of days.

## Configuration

You need to set these environment variables:

- __REPO_OWNER__ - The repository owner
- __REPO_NAME__ - The repository name
- __DAYS_TO_NOTIFY__ - Minimum number of days an pull request needs to be open to send notifications
- __SLACK_CHANNEL_ID__ - Slack channel that will receive the notification
- __SLACK_TOKEN__ - Slack authorization token

## How to run

Just execute:

```python3 main.py```
