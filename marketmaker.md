
(c) 2017 Steemit, Inc.  All rights reserved
CONFIDENTIAL - STEEMIT INTERNAL USE ONLY

We want to design a stabilizing market maker which:

- Provides liquidity to the system
- Stabilizes prices against sudden fluctuations

Consider a community token called the CAT token, popular among feline enthusiasts.
The CAT token is a CBT and therefore trades against STEEM on the blockchain.

MM balances of CAT and STEEM are influenced by two distinct actions:

- *MM market actions* are orders that the MM creates in response to a new user market orders.
- *MM drops* direct CAT tokens or STEEM to the MM in response to blockchain events external to the MM.

# MM market actions

Consider an MM which starts with an initial supply of `T_0` CAT tokens and no STEEM tokens.
As the price increases, the MM sells CAT tokens into the market to build its STEEM reserve.
When the price decreases, the process reverses, and the MM uses the STEEM balance it's accumulated
to purchase CAT tokens.

This MM has a *policy curve* that looks like this:

TODO: Graph

The equation for this policy curve is:

\begin{eqnarray*}
T(p) & = &
\begin{cases}
T_0 & \text{when } p \leq p_0 \\
T_0 \left( {p \over p_0} \right)^r & \text{when } p \geq p_0 \\
\end{cases}
\end{eqnarray*}

We establish $r = \log(0.9) / \log(2)$ and $p_0 = .001$.  This corresponds to a policy of selling
10% of the CAT reserve every time the price of CAT doubles relative to the price of STEEM,
starting when CAT has 0.1% the market cap of STEEM.

TODO:  Table

# Implementation notes

Implementing the MM is non-trivial.  Here is the overall strategy:

- The MM has an inventory of $t$ CAT tokens and $s$ STEEM.
- The current market price is $p$.
- Valuing the MM STEEM inventory at current market prices, its current worth in tokens is $T_0(p) = t + {s \over p}$.
- Compute $T(p)$.
- Buy or sell until we arrive at $T(p)$.

For given values of $s, t$, find the price $p^*$ such that $T(p^*) = t$:

\begin{eqnarray*}
t & = & T(p^*) = T_0 \left( {p^* \over p_0} \right)^r \\
  & = & \left( t + {s \over p^*} \right) \left( p^* \over p_0 \right)^r \\
\Leftrightarrow \log(t) = 
\end{eqnarray*}

- We know $T$ and $T_0$, so we can solve for the policy price $p$.
- Then we buy or sell at the current market price to drive the policy price $p$ to match $q$.

Two questions are whether $T(p)$ 



To begin with, we consider a simplified ideal market where any amount can be bought or sold exactly at $q$
(i.e. infinite depth and zero spread).  This simplifying assumption allows $T_0$ to be constant as any transaction
is carried out.







The implicit price of the MM is 


The price implied by the MM's
*current inventory* is given by $q = T / S$, where $T$ is its inventory of CAT tokens and
$S$ is its inventory of STEEM.

How do MM market actions affect $q$?  Selling CAT for STEEM decreases $q$; buying increases $q$.

Let's consider an idealized market.  $q$ 

- Determine what $q$ should be based on current inventory


then the numerator of $q$ decreases while the denominator increases.  If the MM buys CAT with STEEM, then the reverse happens:
the numerator of $q$ increases while the denominator decreases.

The market 

The MM should interact with the market in a way that drives the market price and $q$ toward
each other.  If the MM is able to buy 






First, solve for $p$ (in units of $p_0$) as a function of $T / T_0$:

\begin{eqnarray*}
\left( {T \over T_0} \right) ^ {1 \over r} & = & {p \over p_0}
\end{eqnarray*}

Call this 



Let us measure $T$ in units of $T_0$ and measure $p$ in units of $p_0$.  This allows us to
simplify our notation, yielding simply $T = p^r$ (or equivalently, $T^{1/r} = p$).

\begin{eqnarray*}
T ^ {1 \over r} & = & p
\end{eqnarray*}






This allows us to take the current state of the market maker's inventory and determine the
price it should be trading at.

Then we 














1/2 ^ (p - p_0)



# MM drops

- CAT drops due to inflation of new CAT tokens
- STEEM drops due to Support



The market maker (MM for short) starts with an initial supply of CAT tokens.



Certain events
may direct additional CAT tokens or STEEM tokens to the market maker's supply


additional CAT tokens or STEEM tokens.  This is called an "MM drop."
The events that cause MM drops to occur will be discussed in a later section.

The only input to determine the market maker's policy is the current price of
CAT to STEEM.  External prices (e.g. in bitcoins or US dollars) are completely
irrelevant to the market maker, thus no price feed is needed for it to operate.

The market maker operates with three assumptions:

- Path independence.







The market maker operates as a *path-independent policy*.







*fiscally responsible*
It only performs trades which result in net profit.

It provides *reactive equilibrium*

For CBT's:

- Provide liquidity to help bootstrap markets for brand-new coin
- Implement 






Initially the market maker is inactive, but it becomes
active at some Steem price `p_0`.



Consider a function $f(r)$ which behaves as $r^2$ when $r$ is close to zero, but as $r$ when $r$ grows toward infinity.
Perhaps $f(r) = r g(r)$ for some function $g(r)$ which is approximately $r$ for small $r$, but approximately unity
for large $r$.  Such a function is $g(r) = {r \over r+1}$, giving $f(r) = {r^2 \over r+1}$.  To get a reward curve with slope bounded
away from zero, similarly to the quadratic case, we shift this curve by some offset $\alpha$ to obtain:

\begin{eqnarray*}
V(r) & = & f(r+\alpha) - f(\alpha) = {(r+\alpha)^2 \over r+1} - {\alpha^2 \over r+1} \\
     & = & {r^2 + 2 \alpha r \over r+1}
\end{eqnarray*}



Suppose we have a market maker which starts out




Market maker keeps balance of CAT and STEEM

Reactively keep STEEM and CAT in balance.



x = log(2**i / 1000)
y = log(.9**i)

x = 2**i / 1000
y = .9**i = e^(log(.9) * i)

i = log_2( 1000*x )
y = e^(log(.9) * log( 1000*x) / log(2) )
  = (1000*x)^



x = 2**i / 1000
y = .9**i

i = log(1000*x) / log(2)
y = exp(log(.9) * log(1000*x) / log(2))


(log(0.001), log(1   ))
(log(0.002), log(0.9 ))
(log(0.004), log(0.81))

dx = log(2)
dy = log(0.10)


