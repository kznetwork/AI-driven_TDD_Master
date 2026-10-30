import time


def now_ms(clock=time.time):           # ✅ 시계를 주입할 수 있게
    return int(clock() * 1000)
