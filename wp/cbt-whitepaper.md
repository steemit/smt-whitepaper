# History of custom tokens

The blockchain of the future will be a friendly environment for entrepreneurs to build businesses based on their own tokens.  The first wave of technology was the first-generation altcoin wave, beginning with the release of Litecoin in (TODO: Litecoin launch year) -- but creating a token means coding and maintaining a separate blockchain from scratch.  In (TODO: BitShares launch year) BitShares pioneered user-issued assets (UIA’s), allowing any user to launch a custom token -- but logic other than simple token ownership had to be done off-chain.  Then in (TODO: Ethereum launch year) Ethereum allows any user to launch a custom token using a Turing-complete smart contract.

The pattern is clear:  Over time, barriers to developing and launching new tokens are dropping.  Token developers want technology that demolishes the barriers to launching a new token.  The purpose of this whitepaper is to describe CBT’s -- Community Building Tokens.  CBT’s are the next step in this evolution.

# Current barriers

The barriers to developing a new blockchain in the current environment include:

- Users of tokens must pay a fee per transaction.
- The “blank slate” of an empty Ethereum contract is intimidating to entrepreneurs.  The entrepreneur’s creativity must come up with (1) the product development skills to create a product that users want, (2) the technical skills to code a rock-solid Ethereum contract, (3) a (TODO: some adjectives here) user interface, (4) the economic skills to design a token supply and inflation model that token holders will accept.
- Iterative development of all of the above based on feedback from user behavior.
- Shared tenancy of many independent projects on a single-threaded blockchain leads to poor performance.
- Distribution problem:  How to get new users into the ecosystem without requiring them to buy your token, while remaining fair to users who have paid for the token?
- “Cold-start” userbase problem:  How do you grow enough to get a meaningful network effect?  If your project requires a certain minimum userbase to be viable, how do you create that?

CBT’s solve all these barriers:

- By leveraging a high-performance in-memory database, parallel execution, and state checkpointing, large transaction capacity within a given hardware resource envelope.  (TODO:  Numbers)
- With Steem’s bandwidth model, no per-transaction fees
- Built-in business model:  Build a community around some shared interest (which can be anything from scuba diving to classical violin)
- Product development, backend technology, UI and economics are similar enough that they are mostly shared across communities.  Therefore costs and benefits of initial development and ongoing iterative improvements in any of these areas may be shared among all communities.
- Multi-threaded implementation allows good performance and minimizes single-core bottlenecks.
- Existing Steem userbase can instantly participate in a new community (solves cold-start userbase problem) and earn tokens by posting / voting (solves distribution problem).

# Defining the growth problem

![Graphical representation of user flow](img/build/userflow.png)


What brings users to a token?

- Functionality:  Some feature, e.g. decentralized pseudonymous value transfer (Bitcoin), market-pegged assets (BitShares), prediction markets (Augur), ability to post/vote and get rewarded (Steem).
- Value:  Token is seen as an asset that will continue to hold/gain value in the future, therefore buying/holding is desirable from a strictly financial standpoint.
- Marketing:  Advertising brings in users.
- Community:  Users want to participate in community discussions (bitcointalk, bitsharestalk, /r/bitcoin, Steem).
- Exclusive market:  Users need/want to do certain transactions that can only occur with the token (e.g. you must pay US taxes in dollars).

What does this mean from a token designer’s perspective?

- Functionality:  Creating new functionality that can be reasonably implemented on a blockchain and that users want is a very hard problem requiring great creativity and market research.
- Value:  Inflation policy is not too generous, token sinks, implicit / explicit pledges by major holders to buy / sell less / not sell at low value.
- Marketing:  TODO
- Community:  Very tough to jumpstart this from scratch.  CBT’s (1) have access to the Steem community as a nucleus of initial users, (2) incentivize participation with low users, (3)







Business

- Use Steem support to buyback tokens
- What is the algorithm for determining Steem support?
- Use percentage of token inflation to buy-and-burn Steem as market cap increases
- Why we need it and it can’t be optional
- On-chain market between Steem and coins

Tech
- Why C# (I have a whitepaper on this for DOT, we can use with little modification)
- Parallelism via two-way sidechaining
- JSON type schemas
- Voting power balance of Steem vs token
- Tokens have vesting, vesting = voting power
- Specification of accesses as function of operation, state, prev operation
- State checkpointing

Steem features considered for cutting:
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


We've come up with an interesting new idea.  Much of the value proposition of Ethereum is in ICO's -- entrepreneurs come up with an idea for a token, market it and sell to users

The killer feature isn't the Turing complete nature, it's being able to launch ICO's.  So what we've decided to do is implement a system where users can set up communities (think subreddits).  A community can be set up to reward users with STEEM as the base site, or can be set up to reward user with a custom token *of that community*, which is issued by the founder of that community -- called CBT (community building token).

The problem with Ethereum, or UIA (user issued asset) on BitShares, is that it's actually too flexible -- it requires the issuer to be creative enough to come up with their own business model.  CBT's give the entrepreneur a business model out of the box -- build a community -- which is repeatable for different areas of interest.









Nathan’ Basic Understanding:
A CBT is a type of user-created currency based on the STEEM blockchain, or a sidechain.. Many people wish to create their own type of currency, but lack the technical skills to do it from scratch, fork and modify an existing technology/blockchain, or create smart contracts in Ethereum.

CBTs will allow users to go through some sort of intuitive setup process and have a custom token created with the options chosen, as well as a special subreddit type board on steemit.

They will be able to have a simplified set of STEEM’s features, and will probably exist on a sidechain of the STEEM blockchain.
