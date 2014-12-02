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


plotcolors = plt.colors()


# def nextplotcolor(i=0):
# def cs():
#         while True:
#             while i >= len(plotcolors):
#                 i -= len(plotcolors)
#             yield plotcolors[i]
#             i += 1
#     return cs
#


def fitfunct(t, a, b, c, d, e):
    return c * np.sin(a * 2 * np.pi * t + d) * np.exp(-b * t) + e

def hull(t, b, c):
    return c * np.exp(-b * t)

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


def plt_config():
    plt.grid(True)
    plt.autoscale(True)
    plt.ylabel(r"Auslenkung $\omega$")
    plt.xlabel(r"Zeit $t$ [s]")
    plt.legend(loc='best')


def process_data(x, y, f=fitfunct, label1="Messwerte", label2="Fit", pnames=['omega', 'gamma']):
    ps, vs = scipy.optimize.curve_fit(f, x, y)
    xvals = np.arange(x[0], x[-1], 1e-3)
    plt.plot(xvals, f(xvals, *ps) - ps[4], label=label2)
    plt.plot(x, y - ps[4], marker=".", ms=2, ls="", label=label1)
    plt.plot(xvals, hull(xvals, ps[1], ps[2]), color='red', label=r'Einhüllende')
    plt.plot(xvals, hull(xvals, ps[1], -ps[2]), color='red')
    # plt.show()
    vals = [(p, vs[i][i]) for i, p in enumerate(ps)]
    if pnames:
        return {name: v for name, v in zip(pnames, vals)}
    else:
        return {"x_%d" % i: p for i, p in enumerate(vals)}


def plot_to_file(x, y=None, fname='o', pname='o', fformat='pdf'):
    if not y:
        fname = pname = x[:-4]
        x, y = data_from_file(x)

    plt.clf()
    params = process_data(x, y, pnames=['omega', 'gamma', 'phi_0'])
    plt_config()
    plt.savefig("%s.%s" % (fname, fformat), format=fformat)
    with open("%s.FitParams.txt" % pname, mode='w+') as f:
        for k in params:
            f.write("%s = %f, Statistischer Fehler: %f\n" % (k, params[k][0], params[k][-1]))


def main():
    datax, datay = data_from_file(filename)

    plot_to_file(datax, datay)
    # plt.grid(True)
    # plt.autoscale(True)

    print(process_data(datax, datay, pnames=["omega", "gamma", "phi_0"]))
    plt_config()
    plt.show()

    # x, y = smooth(data[0], data[1])
    ps, vs = scipy.optimize.curve_fit(fitfunct, datax, datay)
    x = np.arange(0, 22, .001)
    print(ps)
    print(vs)
    a, b, c, d, e = ps
    hull = lambda x, e: e * np.exp(-b * x)  # einhüllende Funktion
    # plt.plot(datax, datay - d, "", x, fitfunct(x, a, b, c, 0, e), "", x, hull(x, e), "", x, hull(x, -e), "")

    for c, v in zip(['a', 'b', 'c', 'd', 'e'], ps):
        print("%c = %f" % (c, v))
    for i in range(5):
        print(vs[i][i])
    # plt.show()
    print()
    pass


if __name__ == '__main__':
    main()