import time
import datetime

start = time.time()

print("Hellow World!")

while True:
    time.sleep(1)
    dt_now = datetime.datetime.now()
    print(dt_now)

