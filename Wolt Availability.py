from selenium import webdriver
from win10toast import ToastNotifier
import time

# MODIFY
driver = webdriver.Edge()  # Modify to Edge / Chrome / FireFox, etc
# target refers to the restaurant we will be running the program on
target = "https://wolt.com/en/isr/tel-aviv/restaurant/burgus-burger-bar-ramat-hachayal"
# endof MODIFY

notifier = ToastNotifier()
driver.get(target)
time.sleep(2)
restaurant = driver.title

while True:
    time.sleep(5)
    if 'Scheduled orders only' in driver.page_source:
        print('Unavailable, trying again in 5 seconds..')
        driver.get(target)
    else:
        print('Available!')
        driver.quit()
        notifier.show_toast("Open for deliveries", restaurant, duration=60)
        break