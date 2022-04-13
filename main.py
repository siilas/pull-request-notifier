import sys

sys.path.append('./sources')

import notification_service

if __name__ == "__main__":
    print("Starting process...")
    notification_service.get_pull_requests_and_send_notifications()
    print("Finishing process...")