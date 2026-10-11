def calc(d, t):
    tmp = 0
    for x in d:
        tmp += x[0] * x[1]
    return tmp * (1 - t)
