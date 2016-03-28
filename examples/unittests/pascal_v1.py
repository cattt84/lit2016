def pascal(n):
    x = 1
    yield x
    for k in range(n):
        x = x*(n-k)//(k+1)
        yield x

if __name__ == '__main__':
    for n in range(7):
        line = ' '.join(map(lambda x: '{:2}'.format(x), pascal(n)))
        print(str(n)+line.center(25))
