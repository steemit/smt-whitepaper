#!/usr/bin/env python3

import collections
import datetime

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FormatStrFormatter

import math

def f(p):
    return (0.9)**(math.log(p) / math.log(2))

F_CBT = 100e3
F_STEEM = 250e6
r = 0.15

# p * F_CBT / F_STEEM

def s(p, i_ratio=1.0):
    f_p = f(p)
    result = (1.0 - f_p) * p * r * F_CBT * i_ratio / (F_STEEM * f_p)
    return result

prices = [math.exp(i/20.0) for i in range(1, 300)]
x = [100 * p * F_CBT / F_STEEM for p in prices]
y_50  = [10000 * s(p, 0.5) for p in prices]
y_100 = [10000 * s(p, 1.0) for p in prices]
y_200 = [10000 * s(p, 2.0) for p in prices]

plt.plot(x, y_50)
plt.plot(x, y_100)
plt.plot(x, y_200)

# One unit of support represents 0.01% of the support in the system

ax = plt.gca()
ax.grid(True)
ax.set_xlim([0.0, 20.0])
ax.set_ylim([0.0, 1000.0])
ax.set_xticks([  2*i for i in range(11)])
ax.set_yticks([100*i for i in range(11)])
ax.xaxis.set_major_formatter(FormatStrFormatter("%d%%"))
ax.yaxis.set_major_formatter(FormatStrFormatter("%d"))
ax.set_xlabel("Market cap relative to STEEM supply")
ax.set_ylabel("Support")

#y = [e["current_supply"] for e in data]
#plt.plot(x, y)

plt.title("Market maker equilibrium")
plt.savefig("img/build/mm-equilibrium.png")
