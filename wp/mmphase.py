#!/usr/bin/env python3

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FormatStrFormatter

import math

# Phase space plot of market maker policy
# Keep track of the Steem

def policy_curve(price):
    return 0.9**(math.log(price) / math.log(2))

def apply_policy(state, price):
    # (cbt, steem) -> (cbt', steem')
    if price < 1:
        return state
    value_cbt = state[0] * price
    value_steem = state[1]
    total_value = value_cbt + value_steem
    f_current = value_cbt / total_value
    f_policy = policy_curve(price)
    delta_cbt_value = (f_policy - f_current) * total_value
    delta_steem = -delta_cbt_value
    delta_cbt = delta_cbt_value / price
    return (state[0] + delta_cbt, state[1] + delta_steem)

class StateCurve(object):
    def __init__(self):
        self.x = []
        self.y = []
        self.xv = []
        self.x_crit = []
        self.y_crit = []
        self.xv_crit = []
        self.p_crit = []
        return

def draw_state_curve(plt, initial_cbt, is_value=False, show_dots=False):
    state = (float(initial_cbt), 0.0)

    curve = StateCurve()

    p = 1.0

    crit_price = 2

    while state[1] < 1200.0:
        curve.x.append(state[0])
        curve.y.append(state[1])
        curve.xv.append(state[0] * p)
        p1 = p*1.001
        if (p1 > crit_price):
            s_crit = apply_policy(state, crit_price)
            curve.x_crit.append(s_crit[0])
            curve.y_crit.append(s_crit[1])
            curve.xv_crit.append(s_crit[0]*p)
            curve.p_crit.append(crit_price)
            crit_price *= 2
        p = p1
        state = apply_policy(state, p)

    if not is_value:
        plt.plot(curve.x, curve.y)
        if show_dots:
            plt.plot(curve.x_crit, curve.y_crit, 'o')
    else:
        plt.plot(curve.xv, curve.y)
        if show_dots:
            plt.plot(curve.xv_crit, curve.y_crit)

    return curve

def draw_double_lines(plt, curve):
    for i in range(len(curve.x_crit)):
        dx, dy = curve.x_crit[i], curve.y_crit[i]
        m = dy / dx
        print(dx, dy, m, 100, 100*m)
        plt.plot([0, 100], [0, 100*m], "k-")

plt.clf()
ax = plt.gca()
ax.grid(True)
ax.set_xlim([0, 100])
ax.set_ylim([0, 1200])
ax.set_xticks([i for i in range(0, 110, 10)])
ax.set_xlabel("Tokens")
ax.set_ylabel("STEEM")

c100 = draw_state_curve(plt, 100, show_dots=True)
c80 = draw_state_curve(plt,  80)
c120 = draw_state_curve(plt, 120)
draw_double_lines(plt, c100)

plt.title("Market maker holdings")
plt.savefig("img/build/mm-phase-adjust.png")

plt.clf()
ax = plt.gca()
ax.grid(True)
ax.set_xlim([0, 100])
ax.set_ylim([0, 1200])
ax.set_xticks([i for i in range(0, 110, 10)])
ax.set_xlabel("Tokens")
ax.set_ylabel("STEEM")

c100 = draw_state_curve(plt, 100, show_dots=True)

plt.title("Market maker holdings")
plt.savefig("img/build/mm-phase.png")

"""
plt.clf()
ax.grid(True)
ax.set_xlim([0, 1000])
ax.set_ylim([0, 1200])
ax.set_xticks([i for i in range(0, 1300, 100)])

plt.plot(xv, y)
plt.plot(xv_crit, y_crit, 'o')
plt.title("Market maker value")
plt.savefig("mm-value.png")
"""
