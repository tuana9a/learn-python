import time
import random
import threading

def read(event: threading.Event):
    i = 0
    while True:
        event.wait()
        print(f"hello world {i}")
        i += 1

def monitor(event: threading.Event):
    while True:
        sleep_time = random.randint(1, 5)
        print('monitor sleep', sleep_time)
        time.sleep(sleep_time)
        event.set()
        event.clear()

lock = threading.Event()

t0 = threading.Thread(target=monitor, args=[lock])
t1 = threading.Thread(target=read, args=[lock])

t0.start()
t1.start()