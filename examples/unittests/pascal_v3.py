def pascal(n):
    x = 1
    yield x
    k = 0
    while n-k != 0:
        x = x*(n-k)/(k+1)
        k = k+1
        yield x
