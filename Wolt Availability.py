import time
from plyer import notification
import requests

def notify_on_crash():
    notification.notify(
        title="Program crashed",
        message="The program has crashed. Please check the logs for more information.",
        timeout=60
    )

website = input("Enter the Wolt web address of the restaurant's page")
i = 0
while True:
    try:
        response = requests.get(website)
        if 'Scheduled orders only' not in response.text:
            notification.notify(
                title="Open for deliveries",
                message=website,
                timeout=60
            )
            break
        else:
            print(f"Unavailable, trying again in 5 seconds.. ({i})")
            i += 1
            time.sleep(5)
    except Exception as e:
        print(f"Error: {e}")
        notify_on_crash()
        break
