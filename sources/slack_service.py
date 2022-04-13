import os
import requests

days_to_notify = os.getenv("DAYS_TO_NOTIFY", "")
slack_channel_id = os.getenv("SLACK_CHANNEL_ID", "")
slack_token = os.getenv("SLACK_TOKEN", "")

headers = { 
    "Content-type": "application/json", 
    "Authorization": "Bearer {token}".format(token = slack_token) 
}

def send_slack_notifications(filtered_pull_requests):
    print("Sending slack notifications...")

    if not slack_channel_id:
        raise Exception("The slack channel id must be set in the enviroment variable: SLACK_CHANNEL_ID") 
    
    if not slack_token:
        raise Exception("The slack authorization token must be set in the enviroment variable: SLACK_TOKEN")
    
    if not days_to_notify:
        raise Exception("The number of days to notify must be set in the enviroment variable: DAYS_TO_NOTIFY")

    data = { "channel": slack_channel_id, "text": __create_notification_message(filtered_pull_requests) }

    requests.post("https://slack.com/api/chat.postMessage", data = data, headers = headers)

def __create_notification_message(filtered_pull_requests):
    message = "There are pull requests open after {days} days. ".format(days = days_to_notify)
    message += "Please, take o look at it ;) \n"

    for pull_request in filtered_pull_requests:
        message += " - <{link}|{title}> \n".format(link = pull_request.html_url, title = pull_request.title)
    
    return message
