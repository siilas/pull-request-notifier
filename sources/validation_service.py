import os
from datetime import datetime

days_to_notify = os.getenv("DAYS_TO_NOTIFY", "")

date_pattern = "%Y-%m-%dT%H:%M:%SZ"

def validate_pull_requests(open_pull_requests):
    print("Validating pull requests...")
    
    if not days_to_notify:
        raise Exception("The number of days to notify must be set in the enviroment variable: DAYS_TO_NOTIFY") 
    
    filtered_pull_requests = []
    
    for open_pull_request in open_pull_requests:
        creation_date = datetime.strptime(open_pull_request["created_at"], date_pattern)
        
        if (__is_creation_date_past_days_to_notify(creation_date)):
            filtered_pull_requests.append(open_pull_request)
    
    return filtered_pull_requests

def __is_creation_date_past_days_to_notify(open_date):
    return (open_date - datetime.today()).days > int(days_to_notify)