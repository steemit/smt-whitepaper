#!/usr/bin/env python3

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import numpy as np

import bisect
import math

class RewardCurvePlotter(object):

    def __init__(self,
        reward_curve=None,
        curation_curve=None,
        xmin=0.0,
        xmax=10000.0,
        xsteps=1000,
        ymin=0.0,
        ymax=None,
        ysteps=1000,
    ):

        self.reward_curve = reward_curve
        self.curation_curve = curation_curve
        self.xmin = xmin
        self.xmax = xmax
        self.xsteps = xsteps
        self.ymin = ymin
        if ymax is None:
            dx = float(xmax - xmin) / float(xsteps)
            ymax = (reward_curve(xmax) - reward_curve(xmax - dx)) / dx
        self.ymax = ymax
        self.ysteps = ysteps
        return

    def plot_curation(self):

        xmin, xmax, xsteps = self.xmin, self.xmax, self.xsteps
        ymin, ymax, ysteps = self.ymin, self.ymax, self.ysteps

        dx = float(xmax - xmin) / float(xsteps)

        #print("ymax:", ymax)

        dy = float(ymax - ymin) / float(ysteps)
        wlist = [0.0]
        img = 0.0 * np.ones((xsteps, ysteps))
        for i in range(xsteps):
            x0 = i*dx
            x1 = x0+dx
            dw = self.curation_curve(x1) - self.curation_curve(x0)
            drc = (self.reward_curve(x1) - self.reward_curve(x0)) / dx
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

class QuadraticRewardCurve(object):
    def __init__(self, s=1.0):
        self.s = s
        self.name = "quadratic"
        return

    def __call__(self, r):
        return r*r + 2.0*r*self.s

class BoundedWeightCurve(object):
    def __init__(self, s=1.0):
        self.s = s
        self.name = "bounded"
        return

    def __call__(self, r):
        return float(r) / float(r + 2.0*self.s)

class LinearCurve(object):
    def __init__(self):
        self.name = "linear"
        return

    def __call__(self, r):
        return float(r)

class SqrtCurve(object):
    def __init__(self):
        self.name = "sqrt"
        return

    def __call__(self, r):
        return math.sqrt(r)

reward_curves = [
    QuadraticRewardCurve(s=0.2),
    LinearCurve(),
    ]

weight_curves = [
    BoundedWeightCurve(s=0.2),
    LinearCurve(),
    SqrtCurve(),
    ]

for rc in reward_curves:
    for cc in weight_curves:
        rcp = RewardCurvePlotter(
            xmin=0.0,
            xmax=1.0,
            reward_curve=rc,
            curation_curve=cc,
            )
        plt.clf()
        rcp.plot_curation()
        plt.title("rc_"+rc.name+" + cc_"+cc.name)
        plt.savefig("rc-"+rc.name+"-cc-"+cc.name+".png")
