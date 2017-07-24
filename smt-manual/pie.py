#!/usr/bin/env python3

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import numpy as np

import bisect
import math

def plot_curation(
    reward_curve=None,
    curation_curve=None,
    xmin=0.0,
    xmax=10000.0,
    xsteps=1000,
    ymin=0.0,
    ymax=None,
    ysteps=1000,
    ):

    dx = float(xmax - xmin) / float(xsteps)

    if ymax is None:
        ymax = (reward_curve(xmax) - reward_curve(xmax - dx)) / dx

    #print("ymax:", ymax)

    dy = float(ymax - ymin) / float(ysteps)
    wlist = [0.0]
    img = 0.0 * np.ones((xsteps, ysteps))
    for i in range(xsteps):
        x0 = i*dx
        x1 = x0+dx
        dw = curation_curve(x1) - curation_curve(x0)
        drc = (reward_curve(x1) - reward_curve(x0)) / dx
        wlist.append(wlist[-1]+dw)

        #print("x0:", x0, "x1:", x1, "drc:", drc)

        epsilon = 1e-5

        for j in range(ysteps):
            y = ymin + (j+0.5) * dy
            #print(x0, y)
            if y < ymin:
                continue
            if y > drc:
                break
            search_val = (1.0 - (y / drc)) * wlist[-1]
            img[j][i] = bisect.bisect_left(wlist, search_val) / float(xsteps+1) + epsilon
            #print(i, j, img[i][j])

    cmap = cm.Paired
    cmap.set_under(color="white")

    plt.imshow(
       img,
       extent=(xmin, xmax, ymin, ymax),
       #aspect="equal",
       origin="lower",
       interpolation="nearest",
       cmap=cmap,
       vmin=2.0*epsilon,
       )
    return

def rc_quadratic(r, s=0.2):
    return r*r + 2*r*s

def cc_quadratic_curation(r, s=0.2):
    return float(r) / float(r+2*s)

def rc_linear(r):
    return float(r)

def cc_linear(r):
    return float(r)

def cc_sqrt(r):
    return math.sqrt(r)

plt.clf()
plot_curation(
    xmin=0.0,
    xmax=1.0,
    reward_curve=rc_quadratic,
    curation_curve=cc_quadratic_curation,
    )
plt.title("rc_quadratic + cc_quadratic_curation")
plt.savefig("quadratic-rewards.png")

plt.clf()
plot_curation(
    reward_curve=rc_linear,
    curation_curve=cc_linear,
    xmin=0.0,
    xmax=1.0,
    ymax=1.2,
    )
plt.title("rc_linear + cc_linear")
plt.savefig("linear-rewards-linear-curation.png")

plt.clf()
plot_curation(
    reward_curve=rc_linear,
    curation_curve=cc_sqrt,
    xmin=0.0,
    xmax=1.0,
    ymax=1.2,
    )
plt.title("rc_linear + cc_sqrt")
plt.savefig("linear-rewards-sqrt-curation.png")
