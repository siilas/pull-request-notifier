import github_service
import validation_service
import slack_service

def get_pull_requests_and_send_notifications():
    try:
        open_pull_requests = github_service.get_open_pull_requests()
        
        if open_pull_requests:
            filtered_pull_requests = validation_service.validate_pull_requests(open_pull_requests.json())
            
            if filtered_pull_requests:
                slack_service.send_slack_notifications(filtered_pull_requests)
            else:
                print("The opened pull requests are up to date...")
        else:
            print("No open pull requests...")
    except Exception as e:
        print("Error:", e)
