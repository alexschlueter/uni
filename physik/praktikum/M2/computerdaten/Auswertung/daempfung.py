#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'fred'

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
from scipy.interpolate import interp1d


filename = "data/2b)ungedämpft.txt"
# filename = "data/3)250mA.txt"
# filename = "data/3)500mA.txt"
# filename = "data/3)1000mA.1.txt"


def fitfunct(t, a, b, c, d, e):
    return e * np.sin(a * 2 * np.pi * t + c) * np.exp(-b * t) + d


def string2float(string):
    string = bytes.decode(string)
    x = str.replace(string, ",", ".")
    return float(x)


def data_from_file(filename=filename, cols=range(2)):
    data = []
    for i in cols:
        data.append(np.genfromtxt(filename, skiprows=2, usecols=i, converters={i: string2float}))
    return data


def smooth(xvals, yvals):  # nicht mehr gebraucht
    f = interp1d(xvals, yvals, kind='cubic')
    x = np.arange(xvals[0], xvals[-1], 1e-3)
    y = f(x)
    return x, y


def main():
    data = data_from_file(filename)
    # x, y = smooth(data[0], data[1])
    ps, vs = scipy.optimize.curve_fit(fitfunct, data[0], data[1])
    x = np.arange(0, 22, .001)
    print(ps)
    print(vs)
    a, b, c, d, e = ps
    hull = lambda x, e: e * np.exp(-b * x)  # einhüllende Funktion
    plt.plot(data[0], data[1] - d, "", x, fitfunct(x, a, b, c, 0, e), "", x, hull(x, e), "", x, hull(x, -e), "")

    for c, v in zip(['a', 'b', 'c', 'd', 'e'], ps):
        print("%c = %f" % (c, v))
    for i in range(5):
        print(vs[i][i])
    plt.show()
    print()
    pass


if __name__ == '__main__':
    main()