__author__ = 'fred'

import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import optimize
import numpy as np


# string2float = lambda b: b.decode().replace(",", ".")
def fitfun(x, a, b, c):
    return c / np.sqrt((x ** 2 - a ** 2) ** 2 + 4 * b ** 2 * x ** 2)


u_f = [(8.07, 0.5353319058),
       (11.02, 0.7710100231),
       (14.00, 0.9871668312),
       (12.50, 0.8818342152),
       (9.50, 0.6622516556),
       (6.50, 0.4242681375)]

us = [x[0] for x in u_f]
fs = [x[1] for x in u_f]

def u_to_f(u):
    uf = lambda u, a, b: a*u + b
    ps, _ = optimize.curve_fit(uf, us, fs)
    return uf(u, *ps)


def string2float(b):
    return float(b.decode().replace(",", "."))


def data_from_file(filename, cols=range(2)):
    data = []
    for i in cols:
        data.append(np.genfromtxt(filename, usecols=i, converters={i: string2float}))
    return data


def process_data(x, y, xerr=0., yerr=0., fitfunc=fitfun, label=""):
    #x = u_to_f(x) * 2*np.pi
    ps, errs = optimize.curve_fit(fitfunc, x, y, p0=[3, 1, 25.5])
    f = lambda x: fitfunc(x, *ps)
    ix = np.arange(np.min(x) - .25, np.max(x) + .25, 1e-3)
    # plt.plot(x, y, marker="x", ls="", label="Messwerte")
    plt.errorbar(x, y, marker="", xerr=xerr, yerr=yerr, ls="", label="Messwerte bei Bremsstrom %s" % label)
    plt.plot(ix, f(ix), label="Fit bei Bremsstrom %s" % label)
    return ps, errs


def config_plt():
    plt.autoscale(True)
    plt.grid(True)
    plt.ylabel("Amplitude")
    plt.xlabel("Motorspannung [V]")
    plt.legend(loc="best", prop={'size': 9})


def main():
    to_file = True
    filename = ("data/5).txt")
    ps1, errs1 = process_data(*data_from_file("data/250mA.txt"), label='250 mA', xerr=0.005, yerr=0.05)
    ps2, errs2 = process_data(*data_from_file("data/750mA.txt"), label='750 mA', xerr=0.005, yerr=0.005)
    print(ps1, ps2)
    print(errs1)
    config_plt()
    if to_file:
        plt.savefig(filename[:-4] + ".pdf", format='pdf')
    plt.show()


if __name__ == '__main__':
    main()