#!/usr/bin/env python3

import collections
import datetime

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FormatStrFormatter

import math

x = [math.exp(i/20.0) for i in range(1, 150)]
#y = [1.0 / (t+1) for t in x]
y = [0.9**(math.log(t) / math.log(2)) for t in x]

for i in range(len(x)):
   print(x[i], y[i])

#plt.axis([0, max(x), 0, 1])

#ax = plt.gca()

plt.plot(x, y)

ax = plt.gca()
ax.set_xscale("log", basex=2)
ax.grid(True)
ax.set_xlim([0.0, 2**10])
ax.set_ylim([0.0, 1.0])
ax.set_xticks([2**i for i in range(11)])
ax.set_yticks([0.1*i for i in range(11)])
ax.xaxis.set_major_formatter(FormatStrFormatter("%d"))
#ax.set_yscale("linear", 

#y = [e["current_supply"] for e in data]
#plt.plot(x, y)

plt.title("Market maker policy")
plt.savefig("mm-policy.png")
