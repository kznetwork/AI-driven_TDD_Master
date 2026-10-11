import time


def timed_call(endpoint, clock=time.perf_counter):
    start = clock()
    endpoint()
    return (clock() - start) * 1000            # ms
