__author__ = 'fred'

from scipy import optimize
from matplotlib import pyplot as plt
import numpy as np
import re


file_num = 4
approx_freq = 4

filenames = map(lambda x: "4)/%i.fit.txt" % x, [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])


def concat_files():
    with open("4)/750ma.txt", "w+") as out_file:
        for fname in filenames:
            with open(fname, "r") as in_file:
                text = in_file.read()
            re_res = re.match(r"Amplitude: (\d\.\d+)\nStatistischer Fehler: (\d\.\d+)", text)
            val, err = re_res.group(1), re_res.group(2)
            out_file.write("%s\t%s\n" % (val, err))


def fit(x, a, b, c, d):
    return b * np.sin(a * x + c) + d


def string2float(b):
    return float(b.decode().replace(",", "."))


def data_from_file(filename, cols=range(2)):
    data = []
    for i in cols:
        data.append(np.genfromtxt(filename, skiprows=2, usecols=i, converters={i: string2float}))
    return data


def process_data(x, y, xerr=0, yerr=0, debug=False):
    ps, es = optimize.curve_fit(fit, x, y, p0=[approx_freq, 1.4, 0, 0])
    print(ps)
    # ***** Debug ******
    if debug:
        f = lambda x: fit(x, *ps) - ps[3]
        ix = np.arange(x[0], x[-1], 1e-4)
        plt.plot(x, y - ps[3], marker=".", ls="")
        plt.plot(ix, f(ix), marker="")
        plt.autoscale(True)
        plt.show()

    return ps[1], es[1][1]
    pass


def main():
    # val, err = process_data(*data_from_file("data/4)/%i.txt" % file_num), debug=True)
    # with open("4)/%i.fit.txt" % file_num, 'w+') as f:
    #     f.write("Amplitude: %f\nStatistischer Fehler: %f\n" % (np.abs(val), err))
    concat_files()

if __name__ == '__main__':
    main()