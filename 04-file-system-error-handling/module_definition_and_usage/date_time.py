import datetime
import time

counter = 0
while counter <= 10:
    curr_time = datetime.datetime.now()
    hour_min_sec = curr_time.strftime("%H:%M:%S")
    print(hour_min_sec)
    counter += 1
    time.sleep(1)
