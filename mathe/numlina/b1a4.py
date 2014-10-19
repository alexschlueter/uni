import math


def f_1(x, y, z):
    return x*(y + z)


def f_2(x, y, z):
    return x * y + x * z


def g_1(x, y, z):
    return x + (y + z)


def g_2(x, y, z):
    return (x + y) + z


def h(n, m):
    return (1 / n) ** m * n ** m - 1

if __name__ == '__main__':
    x = math.e ** 10
    y = math.sin(1.57)
    z = math.log(2.71)
    print('a)\t' + str(f_1(x, y, z) - f_2(x, y, z)))
    x = 10 ** (-10)
    y = 10 ** 10
    z = -y
    print('b)\t' + str(g_1(x, y, z) - g_2(x, y, z)))
    print('c)')
    for n in range(1, 9):
        print('n = ' + str(n) + ':\t' + str(h(n, 10)))
