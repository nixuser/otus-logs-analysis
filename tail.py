import sys
import time

count = 0
while True:
    count += 1
    print(f'time: {time.time()}, count: {count}')
    sys.stdout.flush()
    time.sleep(1)
