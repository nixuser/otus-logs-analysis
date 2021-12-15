import time
import datetime

count = 0
with open('../lines.log', 'w', buffering=1) as f:
    while True:
        count += 1
        f.write(f'time: {datetime.datetime.now():%H:%M:%S %d-%m-%Y}, count: {count}\n')
        time.sleep(1)
