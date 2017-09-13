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
        rewards = [0.0]
        drewards = [0.0]
        s_drewards = [0.0]
        img = 0.0 * np.ones((xsteps, ysteps))
        for i in range(xsteps):
            x0 = i*dx
            x1 = x0+dx
            dw = self.curation_curve(x1) - self.curation_curve(x0)
            r1 = self.reward_curve(x1)
            delta_rc = r1 - self.reward_curve(x0)
            drc = delta_rc / dx

            wlist.append(wlist[-1]+dw)
            rewards.append(0.0)
            total_drewards = 0.0
            for j in range(len(drewards)):
                r_old = rewards[j]
                r_new = (wlist[j+1]-wlist[j]) * r1 / wlist[-1]
                drewards[j] = r_new - r_old
                s_drewards[j] = total_drewards
                rewards[j] = r_new
                total_drewards += drewards[j]
            drewards.append(0.0)
            s_drewards.append(total_drewards)

            #print("x0:", x0, "x1:", x1, "delta_rc:", delta_rc, "drc:", drc, "r1:", r1)
            #print("wlist:", wlist)
            #print("rewards:", rewards, "sum(rewards):", sum(rewards))
            #print("drewards:", drewards, "sum(drewards):", sum(drewards))
            #print("s_drewards:", s_drewards)

            epsilon = 1e-5

            for j in range(ysteps):
                y = ymin + (j+0.5) * dy
                #print(x0, y)
                if y < ymin:
                    continue
                if y > drc:
                    break
                search_val = (1.0 - (y / drc)) * total_drewards
                index = bisect.bisect_left(s_drewards, search_val)
                img[j][i] = index / float(xsteps+1) + epsilon
                #print(x0, y, search_val, index, img[j][i])
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

    def plot_reward_curve(self, *args):
        ax = np.linspace(self.xmin, self.xmax, self.xsteps)
        ay = [self.reward_curve(x) for x in ax]
        plt.plot(ax, ay, *args)
        return

    def plot_curation_curve(self, *args):
        ax = np.linspace(self.xmin, self.xmax, self.xsteps)
        ay = [self.curation_curve(x) for x in ax]
        plt.plot(ax, ay, *args)
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

def copy_bb_aspect(ax_dest, ax_src):
    ( x0,  y0), ( x1,  y1) = ax_dest.get_position().get_points()
    (sx0, sy0), (sx1, sy1) = ax_src.get_position().get_points()
    lx0, lx1 = ax_dest.get_xlim()
    ly0, ly1 = ax_dest.get_ylim()

    slx0, slx1 = ax_src.get_xlim()
    sly0, sly1 = ax_src.get_ylim()

    dest_data_aspect = float(ly1 - ly0) / float(lx1 - lx0)
    dest_bb_aspect = float(y1 - y0) / float(x1 - x0)
    src_data_aspect = float(sly1 - sly0) / float(slx1 - slx0)
    src_bb_aspect = float(sy1 - sy0) / float(sx1 - sx0)

    new_aspect = (src_data_aspect / src_bb_aspect) / (dest_data_aspect / dest_bb_aspect)

    ax_dest.set_aspect( new_aspect )
    return

reward_curves = [
    QuadraticRewardCurve(s=0.2),
    LinearCurve(),
    ]

weight_curves = [
    BoundedWeightCurve(s=0.2),
    LinearCurve(),
    SqrtCurve(),
    ]

figure_letters = 'fdecab'
f = 0

for rc in reward_curves:
    for cc in weight_curves:
        rcp = RewardCurvePlotter(
            xmin=0.0,
            xmax=1.0,
            reward_curve=rc,
            curation_curve=cc,
            )
        plt.clf()
        fig = plt.figure(frameon=False)
        plt.subplots(nrows=3, ncols=1, figsize=(3, 6))
        plt.tight_layout(pad=3.5)

        ax_rc = plt.subplot(3, 1, 1, adjustable="box-forced")
        ax_rc.set_xticklabels([])
        ax_rc.set_yticklabels([])
        plt.title("$\mathbf{Fig. 8"+figure_letters[f]+"}$\nrc_"+rc.name+" + cc_"+cc.name, y=1)
        plt.ylabel("Total reward")
        rcp.plot_reward_curve("k,-")

        ax_cc = plt.subplot(3, 1, 2, adjustable="box-forced")
        ax_cc.set_xticklabels([])
        ax_cc.set_yticklabels([])
        plt.ylabel("Total weight")
        rcp.plot_curation_curve("k,-")

        ax_curation = plt.subplot(3, 1, 3, adjustable="box-forced")
        plt.xlim(rcp.xmin, rcp.xmax)
        plt.ylim(rcp.ymin, rcp.ymax)
        ax_curation.set_xticklabels([])
        ax_curation.set_yticklabels([])
        plt.xlabel("Upvotes")
        plt.ylabel("Marginal reward")
        rcp.plot_curation()

        plt.subplots_adjust(hspace=0.0)

        copy_bb_aspect(ax_rc, ax_curation)
        copy_bb_aspect(ax_cc, ax_curation)

        plt.savefig("rc-"+rc.name+"-cc-"+cc.name+".png", dpi=300)
        f += 1
