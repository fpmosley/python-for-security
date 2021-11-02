import datetime
import time


def current_time():
    curr_time = datetime.datetime.now()
    hour_min_sec = curr_time.strftime("%H:%M:%S")
    print(hour_min_sec)


current_time()
time.sleep(1)
current_time()
time.sleep(1)
current_time()
time.sleep(1)
