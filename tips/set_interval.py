import threading

def set_interval(func, sec, delay=True):
    def func_wrapper():
        set_interval(func, sec)
        func()

    if(not delay):
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
