
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

state = (100.0, 0.0)

x = []
y = []
xv = []
x_crit = []
xv_crit = []
y_crit = []
p_crit = []

p = 1.0

crit_price = 2

while state[1] < 1200.0:
    x.append(state[0])
    y.append(state[1])
    xv.append(state[0] * p)
    p1 = p*1.001
    if (p1 > crit_price):
        s_crit = apply_policy(state, crit_price)
        x_crit.append(s_crit[0])
        y_crit.append(s_crit[1])
        xv_crit.append(s_crit[0]*p)
        p_crit.append(crit_price)
        crit_price *= 2
    p = p1
    state = apply_policy(state, p)

ax = plt.gca()
ax.grid(True)
ax.set_xlim([0, 100])
ax.set_ylim([0, 1200])
ax.set_xticks([i for i in range(0, 110, 10)])

plt.plot(x, y)
plt.plot(x_crit, y_crit, 'o')
plt.title("Market maker holdings")
plt.savefig("mm-holdings.png")

plt.clf()
ax.grid(True)
ax.set_xlim([0, 1000])
ax.set_ylim([0, 1200])
ax.set_xticks([i for i in range(0, 1300, 100)])

plt.plot(xv, y)
plt.plot(xv_crit, y_crit, 'o')
plt.title("Market maker value")
plt.savefig("mm-phase.png")
