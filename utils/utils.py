import time


def measure_time(func, args=None):
    start = time.time()
    result = func() if not args else func(*args)
    end = time.time()

    return end - start, result