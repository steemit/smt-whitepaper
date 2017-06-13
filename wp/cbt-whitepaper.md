# Ned's Notes

Title: Community-Building Tokens - A First Class Meta Token Protocol Built into Steem with Customizeable Economic Properties Specific to Community Buildiong Across Websites and Forums

Sections: 
A. Token Parameters
  1. Reward Pool Inflation Schedule (Annual Inflation; Disinflationary?; Increasingly Inflationary?)
  2. Decentralized Exchange vs. Steem - Bandwidth Costs or Fees or Both -- All Fees go to a Dividends Pool that is paid weekly
  3. Curation Rewards Curve Options and Why you would choose one or the other
  4. Content Rewards Curve Options and Why you would choose one or the other
  5. Will there be a Treasury Committee? And Why? Committee for Arbitrary Rewards - Elect Committee Members who can allocate X% of the Rewards Pool
  6. Payout Dates After Post - 1 Day; 7 Days; 30 Days;
  7. Power/Staking time frames for Power Down - Must be Payout Date Lengths + 1
  8. Savings Account Timelengths - 3 Days? 7 Days? - Will these use exisitng savings account strucutres?
  PLease add more paramters here
  
  Can this really be built in C#? How? Why not C++? We don't need Turing Complete AFAICT.


# Introduction

Steem has proven the value in blockchain-based social media community
which rewards user activity with tokens.  Giving tokens relatively freely
as a reward for participation in the community creates powerful incentive
forces which stoke the growth of the community.

# History of custom tokens

The blockchain of the future will be a friendly environment for entrepreneurs
to build businesses based on their own tokens.  The first wave of technology
was the first-generation altcoin wave, beginning with the release of Litecoin
in (TODO: Litecoin launch year) -- but creating a token means coding and
maintaining a separate blockchain from scratch.

In (TODO: BitShares launch year) BitShares pioneered user-issued assets
(UIA’s), allowing any user to launch a custom token -- but logic other
than simple token ownership had to be done off-chain.  Then in (TODO:
Ethereum launch year) Ethereum allows any user to launch a custom token
using a Turing-complete smart contract.

The pattern is clear:  Over time, barriers to developing and launching new
tokens are dropping.  Token developers want technology that demolishes the
barriers to launching a new token.  The purpose of this whitepaper is to
describe CBT’s -- Community Building Tokens.  CBT’s are the next step in
this evolution.

# Current barriers

The barriers to developing a new blockchain in the current environment include:

- Users of tokens must pay a fee per transaction.
- The “blank slate” of an empty Ethereum contract is intimidating to
entrepreneurs.  The entrepreneur’s creativity must come up with (1) the
product development skills to create a product that users want, (2) the
technical skills to code a rock-solid Ethereum contract, (3) a (TODO:
some adjectives here) user interface, (4) the economic skills to design
a token supply and inflation model that token holders will accept.
- Iterative development of all of the above based on feedback from user behavior.
- Shared tenancy of many independent projects on a single-threaded blockchain
leads to poor performance.
- Distribution problem:  How to get new users into the ecosystem without
requiring them to buy your token, while remaining fair to users who have
paid for the token?
- “Cold-start” userbase problem:  How do you grow enough to get a meaningful
network effect?  If your project requires a certain minimum userbase to be
viable, how do you create that?

CBT’s solve all these barriers:

- By leveraging a high-performance in-memory database, parallel execution,
and state checkpointing, large transaction capacity within a given hardware
resource envelope.  (TODO:  Numbers)
- With Steem’s bandwidth model, no per-transaction fees
- Built-in business model:  Build a community around some shared interest/hobby
(which can be anything from scuba diving to differential equations to
classical violin)
- Product development, backend technology, UI and economics are similar
enough that they are mostly shared across communities.  Therefore costs
and benefits of initial development and ongoing iterative improvements
in any of these areas may be shared among all communities.
- Multi-threaded implementation allows good performance and minimizes
single-core bottlenecks.
- Existing Steem userbase can instantly participate in a new community
(solves cold-start userbase problem) and earn tokens by posting / voting
(solves distribution problem).

# Defining the growth problem

![Graphical representation of user flow](img/build/userflow.png)

What brings users to a token?

- Functionality:  Some feature, e.g. decentralized pseudonymous value
transfer (Bitcoin), market-pegged assets (BitShares), prediction markets
(Augur), ability to post/vote and get rewarded (Steem).
- Value:  Token is seen as an asset that will continue to hold/gain value
in the future, therefore buying/holding is desirable from a strictly
financial standpoint.
- Marketing:  Advertising brings in users.
- Community:  Users want to participate in community discussions
(bitcointalk, bitsharestalk, /r/bitcoin, Steem).
- Exclusive market:  Users need/want to do certain transactions that
can only occur with the token (e.g. you must pay US taxes in dollars).

What does this mean from a token designer’s perspective?

- Functionality:  Creating new functionality that can be reasonably implemented
on a blockchain and that users want is a very hard problem requiring great
creativity and market research.
- Value:  Inflation policy is not too generous, token sinks,
implicit (or explicit) pledges by major holders to sell less (or not sell, or buy)
at low value.
- Marketing:  TODO
- Community:  Very tough to jumpstart this from scratch.  CBT’s (1) have access
to the Steem community as a nucleus of initial users, (2) incentivize participation with low users, (3)

# Market maker function

The CBT blockchain will include an on-chain market to trade CBT's against STEEM.  The blockchain logic
implements a *market maker* to participate in this market.  Each CBT has its own separate market maker.
In this section we will define how the market maker functions.

The market maker is capitalized by a fixed fraction (15%) of CBT inflation, and a variable fraction of
STEEM inflation, determined by user participation in the CBT community.  The STEEM inflation is called
"support."

The market maker has a simple policy:  Every time the price of the CBT doubles, it sells 10% of its holdings.
The market maker also does not trade at very low prices; the price at which the market maker enters the
market is a fixed price called the *entry price* $p_{entry}$.  This policy can be summarized by the following chart:

![Market maker policy curve](img/build/mm-policy.png)\ 

It is informative to look at a *phase space* visualization showing the market maker's CBT inventory and STEEM
inventory on the same diagram.  This diagram was constructed by starting with an inventory of 100 CBT and price
parity (1 STEEM per 1 CBT), then increasing the price in 0.1% increments.  After each increase, exchange STEEM
for CBT at the new price to adjust the STEEM holdings as appropriate to move the percentage of portfolio
value represented by CBT back onto the policy curve.  Moving from right to left, each of the large dots on
the diagram represents a doubling of value relative to the previous dot.

![Market maker phase diagram](img/build/mm-phase.png)\ 

As capital flows into the market maker, the market maker curve shifts up and to the right.  If the new capital
is not in the same STEEM to CBT ratio as the market maker's current inventory, it will buy/sell on the open
market.  Assuming the capital flow is small compared to the market depth (so the market maker's buying/selling
activity is not sufficient to appreciably move the price), this effectively constrains the movement due to capital
changes to occur along lines through the origin, as shown here:

![Market maker phase diagram](img/build/mm-phase-adjust.png)\ 

# Market maker analysis

The market maker is in equilibrium (no buying or selling) when its CBT and STEEM inflows are equal to the portfolio
balance at the current price.  The market maker's CBT input rate is equal to $r \cdot i_{CBT} \cdot F_{CBT}$ where $r = 0.15$ is the fixed
fraction of CBT inflation sent to the market maker, $i_{CBT}$ is the CBT inflation rate, and $F_{CBT}$ is the CBT token
supply.  The market maker's STEEM input rate is equal to $s \cdot i_{STEEM} \cdot F_{STEEM}$ where $s$ is the support
fraction, $i_{STEEM}$ is the STEEM inflation rate, and $F_{STEEM}$ is the STEEM token supply.

The policy fraction is given by the policy curve

\begin{eqnarray*}
f(p) & = & \left( {9 \over 10} \right)^{\log_2(p) - \log_2(p_{entry})}
\end{eqnarray*}

When the market maker is in equilibrium, the price is

\begin{eqnarray*}
r \cdot i_{CBT} \cdot F_{CBT} \cdot f(p) & = &
s \cdot i_{STEEM} \cdot F_{STEEM}
\end{eqnarray*}

To simplify the analysis, let us define the *balanced portfolio price* $p_{bal}$ to be the price at which the market
maker's CBT and STEEM balances are equal.  The BPP occurs at:

\begin{eqnarray*}
p_{bal} & = & {2^{\log(1/2) \over \log(9/10)}} p_{entry} \approx 95.59 p_{entry}
\end{eqnarray*}

At the balanced portfolio price, we have:

\begin{eqnarray*}
r \cdot i_{CBT} \cdot F_{CBT} \cdot p_{bal} & = &
s \cdot i_{STEEM} \cdot F_{STEEM}
\end{eqnarray*}

This is a very interesting relation.  It shows that the constant $r$ actually has a non-obvious alternative interpretation:
It is the support needed to maintain the market maker in equilibrium at the balanced portfolio price!

As blockchain designers, we are now armed with enough information to set the entry price parameter.  Specifically, we can set
some ratio $R$ as the desired capitalization of CBT's relative to STEEM.  Then $p_{bal}$ we may set so that $r R$ is the ratio
of the token value to STEEM:

\begin{eqnarray*}
r R & = & {p_{bal} F_{CBT} \over F_{STEEM}}
\end{eqnarray*}

where $F_{CBT}$ is the current supply of the CBT and $F_{STEEM}$ is the current supply of STEEM.  Running this computation
with $R = 0.25$, $F_{STEEM} = 250,000,000$ and $F_{CBT} = 100,000$ gives $p_{bal} = 93.75$ and $p_{entry} \approx 0.98$.

The interpretation of these numbers is as follows:

- In a healthy market, the aggregate market cap of all CBT's should be about 25% of the value of STEEM.
- If there are a total of 250 million STEEM in existence, the aggregate market cap of all CBT's should be about 62.5 million STEEM.
- If CAT (a particular CBT token devoted to feline enthusiasts) has 15% of the total aggregate support of all CBT's, we want CAT to represent 15% of the 62.5 million STEEM, or 9.375 million STEEM.
- We want the CAT market maker to have a balanced inventory (half of its value in STEEM, half in CAT) when CAT is at 15% of the total aggregate support.
- We don't want the CAT market maker to buy or sell as long as support remains steady at 15%.
- The fact that CAT's inventory is balanced at 15% support means the CAT inflation and the STEEM inflation capital inflows to the market maker must be of equal value, otherwise the MM would buy or sell.
- If CAT and STEEM have the same inflation rate, then the ratio of the inflation inflows is same as the ratio of the token supplies.
- Since we know a ratio of values and a ratio of quantities, dividing these two ratios gives a price.
- Knowing this price allows us to turn the "price" scale from arbitrary relative units to specific concrete units.

We can also invert this calculation.  The support level required to maintain a given 





At a price of $93.75$, the 100,000 CBT tokens in existence are worth
9,375,000 STEEM, or 3.75% of the STEEM supply.



$p_{bal}$ to be the price which makes the CBT market cap equal to 15% of the STEEM market cap.





# Why market makers?

Every new social networking startup faces the problem of turning users into revenue.  The support mechanism
of the market maker -- rewarding the CBT with buy pressure based on user enthusiasm -- solves this problem directly.
It also has ancillary benefits:

- Bootstrap liquidity in the new market.
- Stabilize wild price swings; dampen the effect of price bubbles and sudden sell-offs.

The market maker establishes a *coupling* between market cap and userbase size.  If a particular CBT has support from
5% of the userbase, but only has 1% of the market cap of STEEM, then the market maker will 


- A new CBT will find it far easier to attract users than capital.  Turning
- Bootstrapping a liquid market for a new CBT is non-trivial.



- STEEM holders would like to see some benefit from allowing the CBT to operate on the STEEM platform.


The market maker mechanism solves both problems at a single stroke.  The CBT operator


The market maker mechanism solves some of the central problems of bootstrapping a CBT.





The market maker's policy is essentially to use all its STEEM to buy the CBT as the price goes to zero,
and sell all its CBT for STEEM as the price of the CBT goes to infinity.  In more detail




In this section, we will answer two simple questions:

- How do CBT's benefit from STEEM's ecosystem?
- How do STEEM holders benefit from CBT's?




# Funding the market maker



From the standpoint of a CBT holder:

- CBT's want to get an "updraft" from the powerful economic force that STEEM has already created to bootstrap their value.
- STEEM holders want to be sure to get the value from CBT's.


CBT's face value proposition.


![Graphical representation of value flow](img/build/valueflow.png)






# Business

- Use Steem support to buyback tokens
- What is the algorithm for determining Steem support?
- Use percentage of token inflation to buy-and-burn Steem as market cap increases
- Why we need it and it can’t be optional
- On-chain market between Steem and coins

# Tech

- Why C# (I have a whitepaper on this for DOT, we can use with little modification)
- Parallelism via two-way sidechaining
- JSON type schemas
- Voting power balance of Steem vs token
- Tokens have vesting, vesting = voting power
- Specification of accesses as function of operation, state, prev operation
- State checkpointing

# Steem features considered for cutting:

- All account, witness vote operations unnecessary because accounts deferred to main chain
- Escrow
- Savings
- Mining / PoW
- Vesting routes
- Challenge / prove authority
- Decline voting rights
- Reset_account_operation
- Set_reset_account_operation
- SBD

# Incomplete stuff

The exact economic dynamics of how Steem works is fascinating, rich
theoretical ground.  Explain some of 

What Steem's achieved so far is just the tip of the iceberg.




- Growth coupling:  
- Stimulus effect:  Increased MC incentivizes more posting / commenting
- Demand effect:  Increased userbase generates buy pressure for token

effect is *growth coupling*:  The
token and the community "ride each others' coattails."



Another effect is *oiling the machine*:  Reducing frictional costs


- Growth coupling:  Token / community "ride each others' coattails."
- Oiling the machine:  Reduce / eliminate frictional costs.
- Widening the funnel:  Give low-commitment users (lurkers
and those who don't create an account) a way to effectively participate
- Positive feedback loop



As the token gains more value, users join the community, and
users who view Steem as an investment are happier with their value
and less likely to leave (token -> community coupling).  As users
join the community, they buy and earn the token.  Increased platform
adoption is one of the basic fundamentals of a token, and if this
fundamental indicator is solid,  reassures people the token's fundamentals are solid
causing demand to
increase (community -> token coupling).

Each individual user values his/her contribution according to a certain
amount, if he/she is not getting rewarded "enough" then 


Since the "pie" of currency is
being divided 

This means the currency is
intrinsic value for their contributions


faster than the currency growth.  The currency gains more value as 

Another effect is *positive feedback*:  The community

In the technical section of this whitepaper,
we'll discuss the details of growth coupling and positive feedback loops.



The growth of the community is *coupled* to the growth of the token.  The
exact 
feedback loops

But what Steem's achieved
so far is just the tip of the iceberg:  There's a lot of potential
for similar communities to form




[1] 



existing apps / websites, entrepreneurs, and decentralized organic
growth

Up to this point, the Steem experience has mostly been on
`steemit.com`

We want to make this value proposition widely available


successfully created a blockchain-based

# Another incomplete section

We've come up with an interesting new idea.  Much of the value proposition of Ethereum is in ICO's -- entrepreneurs come up with an idea for a token, market it and sell to users

The killer feature isn't the Turing complete nature, it's being able to build communities with tokens that incentivize growth - whether that be through fundraising (i.e. ICOs; TGEs) or rewards to users (e.g. Steem Content and Curation Rewards).  So what we've decided to do is implement a system where users can set up communities (think subreddits).  A community can be set up to reward users with STEEM as the base site, or can be set up to reward user with a custom token *of that community*, which is issued by the founder of that community -- called CBT (community building token).

The problem with Ethereum, or UIA (user issued asset) on BitShares, is that it's actually too flexible -- it requires the issuer to be creative enough to come up with their own business model.  CBT's give the entrepreneur a business model out of the box -- build a community -- which is repeatable for different areas of interest.

Ned's Comment on "the porblem with....": There are two sepearte problems with Ethereum and UIAs -- Eth allows creativity but it too flexible.  UIAs don't allow creativirty without the creative business being based off-chain.  Any on chain developments are more promising than off chain in the blockchain space.







# Nathan's notes

Nathan’ Basic Understanding:
A CBT is a type of user-created currency based on the STEEM blockchain, or a sidechain.. Many people wish to create their own type of currency, but lack the technical skills to do it from scratch, fork and modify an existing technology/blockchain, or create smart contracts in Ethereum.

CBTs will allow users to go through some sort of intuitive setup process and have a custom token created with the options chosen, as well as a special subreddit type board on steemit.

They will be able to have a simplified set of STEEM’s features, and will probably exist on a sidechain of the STEEM blockchain.
