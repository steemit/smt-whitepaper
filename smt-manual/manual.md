
# Metadata

* CONFIDENTIAL AND PRIVILEGED; DO NOT SHARE
* Originator: Steemit Inc
* Copyright (c) Steemit, Inc. 2017
* Status: DRAFT

# Smart Media Tokens

[Steem](http://steem.io/steem-whitepaper-2-0)’s Smart Media Tokens give anyone the power to launch tokens that make content better, while monetizing that content at the same time. This model, tested and proven by steemit.com and other Steem interfaces, makes monetizing content and media possible in a way never before seen.

Several token protocols, such as Ethereum ERC-20s, allow you to create and launch arbitrary tokens, but no protocol lets content businesses launch tokens that align incentives between users and websites. Due to suboptimal fee structures, private key hierarchies and transaction speeds, none of these protocols could ever provide an acceptable user experience for content websites, such as Twitter, Reddit (even subreddits) or The New York Times.

For content websites and tokens, incentive alignment between websites and users comes from a mathematically guaranteed release of new tokens that must be allocated to the users, including bloggers, vloggers, commenters and curators. The distribution of new tokens occurs based on stake-weighted voting to prevent gaming and eliminate the need for a counterparty. Quality user experience comes from tokens that can be transacted safely (through separate private keys for distinct sets of actions), without fees and at real-time speeds.  Further incentive alignment comes from a company’s ability to raise capital in ICOs, and all Smart Media Tokens have built-in ICO support, should the issuer wish to launch one.

- [Introduction](#introduction)
  - [Leveraging Tokens for Autonomous User Growth](#leveraging-tokens-for-autonomous-user-growth)
  - [New Fundraising Opportunities](#new-fundraising-opportunities)
  - [Immediate Liquidity](#immediate-liquidity)
  - [Can My Entity Participate in SMTs?](#can-my-entity-participate-in-smts)
  - [Use Cases](#use-cases)
    - [1 - Content Publishers - Single Token Support](#1---content-publishers---single-token-support)
    - [2 - Forums - Multiple Token Support](#2---forums---multiple-token-support)
    - [3 - Comments Widget for Online Publishers](#3---comments-widget-for-online-publishers)
    - [4 - Sub-Community Moderators and Managers](#4---sub-community-moderators-and-managers)
    - [5 - IOU Assets - Tokens Representing Real World Assets](#5---iou-assets---tokens-representing-real-world-assets)
- [Owner's manual](#owners-manual)
  - [Establish a Name Space](#establish-a-name-space)
    - [Token consensus](#token-consensus)
  - [Token Generation and Initialized Parameters](#token-generation-and-initialized-parameters)
    - [Creation fee](#creation-fee)
    - [SMT pre-setup](#smt-pre-setup)
    - [SMT setup](#smt-setup)
    - [Token units](#token-units)
    - [Unit ratios](#unit-ratios)
    - [Cap and min](#cap-and-min)
    - [Hidden caps](#hidden-caps)
    - [Generation policy data structure](#generation-policy-data-structure)
    - [Examples and rationale](#examples-and-rationale)
      - [Example ICO](#example-ico)
      - [Why unit ratios?](#why-unit-ratios)
      - [UI treatment of unit ratios](#ui-treatment-of-unit-ratios)
      - [Hidden cap FAQ](#hidden-cap-faq)
    - [Launch](#launch)
    - [Full JSON examples](#full-json-examples)
      - [ALPHA](#alpha)
      - [BETA](#beta)
      - [GAMMA](#gamma)
      - [DELTA](#delta)
      - [Vesting contributions](#vesting-contributions)
      - [Burning contributed STEEM](#burning-contributed-steem)
      - [Vesting as cost](#vesting-as-cost)
      - [Non-STEEM & Hybrid ICO's](#non-steem--hybrid-icos)
    - [Inflation Parameters](#inflation-parameters)
      - [Possible inflation target](#possible-inflation-target)
      - [Event sequences](#event-sequences)
      - [Adding relative inflation](#adding-relative-inflation)
      - [Adding time modulation](#adding-time-modulation)
      - [Inflation operations](#inflation-operations)
      - [Inflation FAQ](#inflation-faq)
    - [Named token parameters](#named-token-parameters)
  - [Parameter constraints](#parameter-constraints)
  - [SMT vesting semantics](#smt-vesting-semantics)
  - [Content rewards](#content-rewards)
  - [Curve definitions](#curve-definitions)
  - [Target votes per day](#target-votes-per-day)
  - [Votability and Rewardability](#votability-and-rewardability)
  - [Hardcoded Token Parameters](#hardcoded-token-parameters)
  - [Mandatory token parameters](#mandatory-token-parameters)
    - [Arbitrary Reward Splitting](#arbitrary-reward-splitting)
  - [SMT interaction with existing operations](#smt-interaction-with-existing-operations)
- [Decentralized Exchange](#decentralized-exchange)
  - [Automatic Order Matching](#automatic-order-matching)
  - [Diverse Asset Types](#diverse-asset-types)
  - [Zero Trading Fees](#zero-trading-fees)
- [Ecosystem Support](#ecosystem-support)
  - [How to Integrate SMTs](#how-to-integrate-smts)
    - [APIs and Documentation](#apis-and-documentation)
    - [Shared Tools for Signup, Key Signing and Wallet Functions](#shared-tools-for-signup-key-signing-and-wallet-functions)
  - [How to Integrate Content from Steem into Websites and Apps](#how-to-integrate-content-from-steem-into-websites-and-apps)
- [Conclusion](#conclusion)
- [References](#references)
- [Appendix](#appendix)
  - [Implementation Notes](#implementation-notes)
  - [Unit Tests](#unit-tests)

- Github: https://github.com/steemit/smt-whitepaper/blob/collab/smt-manual/manual.md
- Git Changes: https://github.com/steemit/smt-whitepaper/commit/6eab36d3b941f52f65e78f3be72efdd5bf5afc2e

# Introduction

Smart Media Tokens (SMTs) is a proposal to build a meta-token protocol on the Steem blockchain. Inspired by the revolutionary properties of the STEEM token, including automatic distributions to content creators, SMTs will be an upgrade beyond previously created blockchain token protocols due to carefully designed token sale programmability, automated liquidity providers and dynamic token distribution parameters as well as a large ecosystem of tools (open source wallets, shared key signing tools, etc.) for integrations at website and application layers.

SMTs are an evolution of the successful relationship established between STEEM and the social websites sitting atop of it, such as steemit.com, which has grown to be a top 2500 website in Alexa rankings in less than one year solely from integrating the incentive model of STEEM. With SMTs, any website or content library across the internet may have one or more tokens integrated into its interface to facilitate fundraising and autonomous growth.

These tokens are designed to allow website operators flexibility during the integration of the token into their community by choosing from many parameters that may be structured creatively at outset or refined over time. Any tokens launched as SMTs shall benefit from a blockchain ecosystem built with an inbuilt decentralized exchange as well as an ecosystem of open-source applications and libraries to support successful deployment, fundraising and growth.

## Leveraging Tokens for Autonomous User Growth

SMTs are a breakthrough for bridging the world's content applications to tokens in a way that aligns incentives between the users of a network and the entrepreneurs building the applications. By leveraging the concepts of inflation and token allocations by post-based voting, SMTs exist in a manner where value must be distributed to users who are participating in their related content networks and applications. Entrepreneurs may now create tokens to integrate with their blog, application or an entire network of applications and topics. And with SMTs the entrepreneurs have the flexibility to decide the economics of the tokens they integrate into their products, from the inflation rates to the algorithms that distribute the tokens.

Entrepreneurs and established entities may rely on SMTs to grow their content network because of the automated and continuous generation of new units of the token that are allocated to producers of content by the holders of the existing tokens through the process of competitive voting. As the tokens are distributed to users of the network, the interests of existing token holders are further aligned with content creators, the businesses running the applications and the entrepreneurs that support them. These unique properties of the tokens’ economics continue to provide incentives for new users to join and participate in growing the network. Any application, whether it is an existing publisher behemoth or a stealth-mode social media startup, will be able to integrate and leverage these special tokens for their own growth.

## New Fundraising Opportunities

Blockchain-based tokens, beginning strongly with the advent of ERC20s on Ethereum, represent a new manner of bringing capital into an organization through the process of Initial Coin Offerings (ICOs). ICOs are an opportunity for one group to sell an initial supply of tokens, privately or publically, for-specific-purpose, for-profit or not-for-profit. Depending on how these tokens are sold, different regulatory bodies could see them as commodities, securities, derivatives or as none of the above. Regardless, it is clear we have seen north of one billion dollars (USD) raised through ICOs in 2017, and to support this trend, it is possible to conveniently launch and sell tokens via the built in ICO contract of SMTs. The launch of SMTs can be structured for ICOs with hard, soft and no caps, and can be tailored to receive STEEM and cryptocurrencies on other blockchains.

## Immediate Liquidity

By leveraging a recently discovered automated market maker concept [1], SMT-based ICOs allow a portion of STEEM tokens received to be sent into an SMT’s on-chain market maker and taker in order to provide liquidity to the SMT at a specified reserve ratio. Beyond the social and specialized distribution mechanisms of SMTs, this feature advances the concept of automated market makers by design; Instead of existing only as the sole actor inside a market, the SMT market maker smart contract acts as a participant inside the SMT’s decentralized markets, which also facilitate bid and asks by human participants.

## Can My Entity Participate in SMTs?
An SMT can be launched by a person or entity; she only needs $1000 to cover the network fee (this prevents spam and unused tokens) and a namespace on Steem, which can be obtained by registering at anon.steem.network, steemit.com, steemconnect.com, or any other Steem sign-up service.

Once the desired name space is secured, the entity issues the token by using a Steem-based Command Line Tool or another tool created in the future for token launches. The token can be structured to support an initial sale or distribution of the token. Certain properties of an SMT, such as its inflation rate, must also be defined by the person or entity creating the token. These properties dictate how the token is used inside applications and respective communities.

From launch, the token becomes immutable on the blockchain, and leveraged correctly, the token can have dramatic effects on the growth of businesses that choose to integrate these tokens.

## Use Cases

We have identified five ways in which existing businesses and future entrepreneurs can leverage specially designed SMTs to transform the internet. Among these use cases you may notice other ways of structuring and leveraging tokens inside applications. This list is by no means exhaustive and we will update this paper as more use cases demonstrate their value.

### 1 - Content Publishers - Single Token Support

A mainstream media website's growth has been slowing and they are looking for ways to get ahead of the changing tech landscape. The website migrates to a Disqus-like application based on Steem or taps directly into Steem APIs for a custom integration. Now their subscribers can be rewarded with crypto currency while commenting. When the website is ready, they can issue their own token through the comments interface - the token will allow them to 1) raise capital by selling tokens 2) catalyze autonomous growth.

![Single Token Content Publishers wireframe](img/uc1-Content-Publishers.png)

### 2 - Forums - Multiple Token Support

An up and coming forum business is looking to integrate cryptocurrency to create cash flow and spark growth to get the business to the next level. They issue an SMT and integrate it into their website, however, they are not cryptocurrency security experts and would prefer not to host a cryptocurrency wallet. Focusing solely on the social aspects, the forum business can integrate other applications, such as SteemConnect, into their forum to handle wallet and transfer capabilities. This allows the forum to focus on their business (growing communities) without focusing on the security aspects of cryptocurrency. The forum enables additional tokens to be exposed or launched to represent specific topics of discussion. The ability to launch these tokens can be retained by the company behind the website or granted to the website's community managers. Tokens dedicated to the website's specific topics will further spur autonomous growth of the website niche by niche. An example of this multi-token model could eventually be found in organizations such as Busy (busy.org) if it were to enable its own globally available token on its domain as well as narrowly available tokens for specific community niches, such as "gardening."

![Multiple tokens Forum wireframe](img/uc2-Forums.png)

### 3 - Comments Widget for Online Publishers

One of the ways in which publishers will be onboarded faster to SMT integrations is by offering a Steem-based comments widget that can easily be integrated into existing blogs that are built on software such as WordPress and Blogger. The developer employing the widget would be able to take a percentage of the tokens (called “arbitrary fees”) distributed to the commenters for themselves, thereby creating a business opportunity for the next generation of Disqus-like companies that are cryptocurrency enabled. It would alleviate the burdens of transaction signing support, private key management, wallet functionality and hosting costs for the publisher by outsourcing these to the comments widget maintainer.

![Comment Widget wireframe](img/uc3-Comment-Widget.png)

### 4 - Sub-Community Moderators and Managers

Imagine you are a moderator for a specific topic inside a forum, such as a Reddit "subreddit" or a Steemit "community". If the main website integrates SMTs for these specific topics, then the moderator/s can launch these tokens to empower the subscribers of their topic, raise funds and increase the quality of content curation for the community.

![Sub-community wireframe](img/uc4-subcommunity.png)

### 5 - IOU Assets - Tokens Representing Real World Assets

An entrepreneur is looking to provide liquidity in the Steem ecosystem. They issue an SMT without inflation properties and imply that they will provide structure to peg it to the USD, making it like an IOU or basic derivative. The structure they provide to the asset includes buying and selling it near $1, similar to Tether. The entrepreneur sets up bank wire capabilities for buying and selling and takes a small % on each transaction. The derivative trades against STEEM and also brings capital into the ecosystem to be used across tokens.

![IOU Asset Token Exchange wireframe](img/uc5-IOU-assets.png)

# Owner's manual

This manual will explain the nuts and bolts of how SMTs work.
The intended audience is technical users who want to create their
own SMT.

## Establish a Name Space

After you've decided on a name for your SMT, you are ready to create
the SMT's *control account*.  This control account will be able to
design the SMT's policies, launch the SMT, and modify certain SMT
parameters after launch.

The SMT's name will be the same as the name of its control account.

### Token consensus

Since tokens participate in atomic transactions also involving
STEEM, they have been designed as part of the STEEM
blockchain's consensus.

## Token Generation and Initialized Parameters

### Creation fee

Issuing an `smt_setup_operation` requires payment of `smt_creation_fee`.
The current `smt_creation_fee` is set by the `smt_creation_fee` field of
`dynamic_global_properties_object`.  This field may contain a value in STEEM
or SBD.  If specified in SBD, an equivalent amount of STEEM will be accepted,
at the current price feed.

Initially, `smt_creation_fee` will be set to 1000 SBD, and no means will be
provided to update it.  Updates to the `smt_creation_fee` amount may occur
in future hardforks, however, so user-agents should read the `smt_creation_fee`
value from the `dynamic_global_properties_object`.  User-agents should not assume
the fee will always be 1000 SBD.

The reason for this fee is to minimize creation of spam assets.

The fee is destroyed by sending it to `STEEMIT_NULL_ACCOUNT`.

### SMT pre-setup

Two pre-setup operations are included:  `smt_setup_inflation_operation` and
`smt_setup_parameters`.  These operations must be issued before
`smt_setup_operation`.  They may be issued in the same transaction, or in
prior blocks.

The reason pre-setup operations are not made a part of `smt_setup_operation`
is to allow a large number of pre-setup operations to be executed over multiple
blocks.

### SMT setup

Each SMT has an associated descriptor object which has
*permanent configuration data*.  This data cannot be changed after launch!
The descriptor is set by the `smt_setup_operation`:

```
struct smt_setup_operation
{
   account_name_type       control_account;
   uint8_t                 decimal_places = 0;
   int64_t                 max_supply = STEEMIT_MAX_SHARE_SUPPLY;

   smt_generation_policy   initial_generation_policy;

   time_point_sec          generation_begin_time;
   time_point_sec          generation_end_time;
   time_point_sec          announced_launch_time;

   asset                   smt_creation_fee;

   extensions_type         extensions;
};
```

The operation must be signed by the `control_account` key.  The name
of the control account becomes the name of the token.  The
`decimal_places` field is used by UI's to display units as a number
of decimals.

The `generation_begin_time` is when participants can begin to contribute
to the ICO.  It is allowed to be in the future so users have time
to study the ICO's final terms before the ICO begins.

The `generation_end_time` is when the ICO stops accepting contributions,
and the `announced_launch_time` is when the ICO token is created (assuming
the ICO reached the minimum participation level).  Some pause is allocated
between the `generation_end_time` and `announced_launch_time` to allow for
the possibility of ICO's that wish to have hidden caps that aren't revealed
while the ICO is open for contributions.  It also gives the ICO creator
time to use the final ICO numbers to aid in pre-launch business
activities.

### Token units

Initial token generation is driven by a contributions of *STEEM
units* from contributors.  To simplify rounding concerns, a
contribution must be an integer number of STEEM units.  The ICO
creator sets the size of a STEEM unit, it can be large or small.
It is better to keep the unit small (for example, 1 STEEM or
0.1 STEEM), as this allows the ICO to be accessible to the
maximum possible audience.

A STEEM unit also specifies a *routing policy* which determines
where the STEEM goes when the token launches.  (STEEM for tokens
which do not launch may be refunded on demand.)  The routing
policy may split the STEEM in the unit among multiple parties.

When the ICO occurs, the tokens are generated in *token units*.
Multiple token units are generated per STEEM unit contributed.
Token units also have a routing policy.

The units and their routing policies are specified in the
`smt_generation_unit` structure:

```
struct smt_generation_unit
{
   flat_map< account_name_type, uint16_t >        steem_unit;
   flat_map< account_name_type, uint16_t >        token_unit;
};
```

Each `(key, value)` pair in the `flat_map` determines the routing
of some satoshis.  The total STEEM/tokens in each unit is
simply the sum of the values.

### Unit ratios

When an SMT launches, token units are created for STEEM
units in an R-for-1 ratio.  The number R is called the
*unit ratio*.  Maximum and minimum allowable values for
R are specified respectively in the `min_unit_ratio`
and `max_unit_ratio` fields of `smt_generation_policy`.

The maximum number of token units that can be created in the ICO
is limited to `max_token_units_generated`, a parameter which is set by
the ICO creator.  (More tokens can be created after the
token has launched, but this later creation is called *inflation*
and is not considered to be part of the ICO.)

The unit ratio is set to the largest integer that would
not result in exceeding `max_token_units_generated` for the number
of STEEM units actually contributed.

### Cap and min

ICO's may specify a minimum number of STEEM units `min_steem_units`.
If the ICO does not reach `min_steem_units` before `generation_end_time`,
then it does not occur and contributors become eligible for refunds.

Likewise, ICO's may specify two maximum numbers of STEEM units:
A *hard cap* and a *soft cap*.  Units in excess of the soft cap
have different routing for their STEEM and tokens.  STEEM units in
excess of the hard cap are rejected and do not generate any SMT's.

The effects of the soft cap are divided proportionally among
all contributors.  I.e. if a ICO has a soft cap of 8 million
STEEM, and 10 contributors each contribute 1 million STEEM,
then 0.2 million of *each user's* STEEM is routed via the
soft cap's policy.

The effects of the hard cap fall solely on the last contributors.
I.e. if a ICO has a hard cap of 8 million STEEM, and 10 contributors each
contribute 1 million STEEM, then the first 8 users fully participate
in the ICO, and the last 2 users are refunded 1 million STEEM.

### Hidden caps

The min and hard cap are *hidden* in the generation policy.  This means
that these numbers are fixed at setup time, but the ICO creator has the
option to keep it secret.  This functionality is implemented by a
*commit/reveal* cryptographic protocol:  A hash called the *commitment*
is published at setup time, and the actual amount must match the
commitment.  (A nonce is also included in the hash to prevent an attacker
from finding the hidden cap with a brute-force guess-and-test approach.)

The SMT designer may wish to pre-publish a guarantee that the hidden
values are within a certain range.  The `lower_bound` and `upper_bound`
fields provide this functionality:  A revealed amount that is not in
the specified range is treated the same as a hash mismatch.

```
struct smt_cap_commitment
{
   share_type            lower_bound;
   share_type            upper_bound;
   digest_type           hash;
};

struct smt_revealed_cap
{
   share_type            amount;
   uint128_t             nonce;
};

struct smt_cap_reveal_operation
{
   account_name_type     control_account;
   smt_revealed_cap      cap;

   extensions_type       extensions;
};
```

All caps are hidden, but the cap may be revealed at any point in time.
Therefore, a ICO with a non-hidden minimum or cap may be implemented by
simply including the `smt_cap_reveal_operation` in the same transaction
as the `smt_setup_operation`.  UI's should provide functionality for this.

A UI should provide one or more of the following means to ensure the `nonce`
and `amount` are recoverable:

- Force the user to type in the `amount` and `nonce` again as confirmation they have been backed up
- Set `nonce` to some deterministic function of the private key and public data, for example
`nonce = H(privkey + control_account + lower_bound + upper_bound + current_date)`
- Provide functionality to brute-force the uncertain fields when the nonce is known (e.g. the current date and `amount`)
- Require the amount to be low-entropy to facilitate brute-forcing when the nonce is known (e.g. a number between 1-999 times a power of 10)

### Generation policy data structure

The SMT generation policy data structure looks like this:

```
struct smt_capped_generation_policy
{
   smt_generation_unit pre_soft_cap_unit;
   smt_generation_unit post_soft_cap_unit;

   smt_cap_commitment  min_steem_units_commitment;
   smt_cap_commitment  hard_cap_steem_units_commitment;

   uint16_t            soft_cap_percent = 0;

   uint32_t            min_unit_ratio = 0;
   uint32_t            max_unit_ratio = 0;

   extensions_type     extensions;
};
```

Note, the `max_token_units_generated` parameter does not appear anywhere in the operation.
The reason is that it is actually a derived parameter,
`max_token_units_generated = min_unit_ratio * hard_cap_steem_units`.

Additionally, the `smt_generation_policy` is defined as a `static_variant` of which
`smt_capped_generation_policy` is the only member:

```
typedef static_variant< smt_capped_generation_policy > smt_generation_policy;
```

This `typedef` allows the potential for future protocol versions to allow additional
generation policy semantics with different parameters.

### Examples and rationale

#### Example ICO

ALPHA wants to sell a token to the crowd to raise funds
where 7% of contributed STEEM goes to Founder Account A, 23% of contributed STEEM
goes to Founder Account B, and 70% of contributed STEEM goes to Founder Account C.

ALPHA defines a STEEM unit as:


```
steem_unit = [["founder_a", 7], ["founder_b", 23], ["founder_c", 70]]
```

This STEEM-unit contains 100 STEEM-satoshis, or 0.1 STEEM.

For every 1 STEEM contributed, an ALPHA contributer will receive 5
ALPHA tokens, and Founder Account D will receive 1 ALPHA token.  This
five-sixths / one-sixth split is expressed as:

```
token_unit = [["$from", 5], ["founder_d", 1]]
```

This ratio is defined in the following data structure:

```
struct smt_generation_unit
{
   flat_map< account_name_type, uint16_t >        steem_unit;
   flat_map< account_name_type, uint16_t >        token_unit;
};
```

This token-unit contains 6 ALPHA-satoshis, or 0.0006 ALPHA (if ALPHA
has 4 decimal places).

Next we define the *unit ratio* as the relative rate at which `token_unit`
are issued as `steem_unit` are contributed.  So to match the specification
of 6 ALPHA per 1 STEEM, we need to issue 1000 ALPHA-units per STEEM-unit.
Therefore the unit ratio of this ICO is 1000.  This unit ratio is placed in
the `min_unit_ratio` and `max_unit_ratio` fields of the
`smt_capped_generation_policy` data structure:

```
min_unit_ratio = 1000
max_unit_ratio = 1000
```

A special account name, `$from`, represents the contributor.  Also
supported is `$from.vesting`, which represents the vesting balance
of the `$from` account.

#### Why unit ratios?

Why does the blockchain use unit ratios, rather than simply specifying
prices?

The answer is that it is possible to write ICO definitions for which
price is ill-defined.  For example:

- `"$from"` does not occur in `token_unit`
- `"$from"` occurs in both `token_unit` and `steem_unit`
- A combination of `"$from"` and `"$from.vesting"` occurs
- Future expansion allows new special accounts

All of these ICO definitions have a unit ratio, but defining a
single quantity to call "price" is complicated or impossible for
ICO's like these.

#### UI treatment of unit ratios

As a consequence of the above, the concept of "ICO price" is purely
a UI-level concept.  UI's which provide a ICO price should do the following:

- Document the precise definition of "price" provided by the UI
- Be well-behaved for pathological input like above
- Have a button for switching between a unit ratio display and price display

#### Hidden cap FAQ

- Q: Should my ICO have a cap?
- A: Some set of people stay away from uncapped ICO's due to perceived "greed",
or want a guaranteed lower bound on the percentage of the ICO their
contribution will buy.  If you want this set of people to participate,
use a cap.

- Q: Should my cap be hidden?
- A: Some people like the transparency and certainty of a public cap.
Other people think a hidden cap creates excitement and builds demand.  One
possible compromise is to publish the previous and next power of 10, for example
"this ICO's cap is between 1 million and 10 million STEEM."

- Q: How do I disable the cap?
- A: Set it so that the cap would occur above `STEEMIT_MAX_SHARE_SUPPLY`.

### Launch

The *effective launch time* is the time at which tokens become transferrable.
Two possibilities occur based on the timing of revealing of the hard cap:

- When `min_steem_units` and `hard_cap_steem_units` are revealed before the
`announced_launch_time`, the launch is an *on-time launch*.  The launch
logic is executed by the blockchain as soon as `announced_launch_time`
arrives, regardless of further user action.
- When `min_steem_units` and `hard_cap_steem_units` have not been revealed
before the `announced_launch_time`, the launch will be a *delayed launch*.
The launch logic is executed by the blockchain when `min_steem_units` and
`hard_cap_steem_units` have been revealed.
- If the launch is delayed, then any contributor may use `smt_refund_operation`
to get their STEEM back at any time after `announced_launch_time` and before
the launch logic is executed.

The reasons for this design are as follows:

- The hidden cap isn't published immediately (that's the definition of *hidden*).
- Publishing the hidden cap is an action that must be done by the ICO creator
(again, any action requiring non-public information to occur cannot happen
automatically on a blockchain).
- If the ICO creator never acts, then the launch logic will never execute.
- In the case of such a malicious or unresponsive ICO creator, contributors'
STEEM would effectively be trapped forever, and they would never receive any tokens.
- To keep the STEEM from being trapped in this way, the `smt_refund_operation`
is implemented.

```
struct smt_refund_operation
{
   account_name_type       contributor;
   account_name_type       control_account;

   asset                   amount;

   extensions_type         extensions;
};
```

Note, users are not *required* to use `smt_refund_operation`; each individual
contributor must opt-in to receiving a refund.  If the ICO creator publicizes a
legitimate reason they failed to publish before `announced_launch_time`, it is
possible that all/most contributors will voluntarily choose not to use
`smt_refund_operation`.  In this case, the launch will occur as soon as the ICO
creator publishes the hidden values.

The launch logic considers a contribution followed by a refund to be
equivalent to not having contributed at all.  Therefore, when a delayed launch
occurs, each contributor will be in *exactly one* of the following two states:

- The contributor has executed `smt_refund_operation`, received their STEEM back,
and will not participate in the ICO
- The contributor has not been issued a refund, and will participate in the ICO

It is possible for a delayed launch to have exceeded its
`min_steem_units` value at the announced launch time, but subsequently
falls below its `min_steem_units` value as a result of refunds.  In such
a case, the ICO will not occur; it will be treated as if it had never
reached its `min_steem_units`.

### Full JSON examples

#### ALPHA

This example builds on the ALPHA example from earlier.  This ICO
has the following characteristics:

- 7% of contributed STEEM goes to Founder Account A
- 23% of contributed STEEM goes to Founder Account B
- 70% of contributed STEEM goes to Founder Account C
- Minimum unit of contribution is 0.1 STEEM
- For every 1 STEEM contributed, the contributor gets 5 ALPHA
- For every 1 STEEM contributed, Founder Account D gets 1 ALPHA
- No minimum, hard cap, or soft cap
- No post-launch inflation after launch

These are the operations for the ALPHA launch:

```
[
 ["smt_setup",
  {
   "control_account" : "alpha",
   "decimal_places" : 4,
   "max_supply" : "1000000000000000",
   "initial_generation_policy" : [0,
    {
     "pre_soft_cap_unit" : {
      "steem_unit" : [["founder_a", 7], ["founder_b", 23], ["founder_c", 70]],
      "token_unit" : [["$from", 5], ["founder_d", 1]]
     },
     "post_soft_cap_unit" : {
      "steem_unit" : [],
      "token_unit" : []
     },
     "min_steem_units_commitment" : {
      "lower_bound" : 1,
      "upper_bound" : 1,
      "hash" : "32edb6022c0921d99aa347e9cda5dc2db413f5574eebaaa8592234308ffebd2b"
     },
     "hard_cap_steem_units_commitment" : {
      "lower_bound" : "166666666666",
      "upper_bound" : "166666666666",
      "hash" : "93c5a6b892de788c5b54b63b91c4b692e36099b05d3af0d16d01c854723dda21"
     },
     "soft_cap_percent" : 10000,
     "min_unit_ratio" : 1000,
     "max_unit_ratio" : 1000,
     "extensions" : []
    }
   ],
   "generation_begin_time" : "2017-08-10T00:00:00",
   "generation_end_time" : "2017-08-17T00:00:00",
   "announced_launch_time" : "2017-08-21T00:00:00",
   "smt_creation_fee" : "1000.000 SBD",
   "extensions" : []
  }
 ],
 ["smt_cap_reveal",
  {
   "control_account" : "alpha",
   "cap" : { "amount" : 1, "nonce" : "0" },
   "extensions" : []
  }
 ],
 ["smt_cap_reveal",
  {
   "control_account" : "alpha",
   "cap" : { "amount" : "166666666666", "nonce" : "0" },
   "extensions" : []
  }
 ]
]
```

Some things to note:

- We disable the soft cap by setting `soft_cap_percent` to `STEEM_100_PERCENT = 10000`
- `post_soft_cap_unit` must be empty when the soft cap is disabled
- The unit ratio does not change so `min_unit_ratio` / `max_unit_ratio` must be set accordingly
- We disable the hidden caps by using a zero nonce and setting `lower_bound == upper_bound`
- We still need to reveal the caps with `smt_cap_reveal_operation`
- The hard cap specified is the largest hard cap that does not result in created tokens exceeding `STEEMIT_MAX_SHARE_SUPPLY`

#### BETA

The BETA token is created with the following rules:

- For every 5 STEEM contributed, 3 STEEM go to founder account Fred
- For every 5 STEEM contributed, 2 STEEM go to founder account George
- 10% of the initial token supply goes to founder account George
- 20% of the initial token supply goes to founder acconut Henry
- 70% of the initial token supply is divided among contributors according to their contribution
- Each STEEM unit is 0.005 STEEM
- Each token unit is 0.0010 BETA
- The minimum raised is 5 million STEEM units, or 25,000 STEEM
- The maximum raised is 30 million STEEM units, or 150,000 STEEM
- Each contributor receives 7-14 BETA per STEEM contributed, depending on total contributions.
- George receives 1-2 BETA per STEEM contributed, depending on total contributions.
- Harry receives 2-4 BETA per STEEM contributed, depending on total contributions.
- If the maximum of 30 million STEEM units are raised, then `min_unit_ratio = 50` applies
- The maximum number of token units is `min_unit_ratio` times 30 million, or 1.5 billion token units
- Since each token unit is 0.0010 BETA, at most 1.5 million BETA tokens will be generated.
- If 75,000 STEEM or less is contributed, the contributors, George and Harry will receive the maximum of 14, 2, and 4 BETA per STEEM contributed (respectively).
- If more than 75,000 STEEM is contributed, the contributors, George and Harry will receive BETA in a 70% / 10% / 20% ratio, such that the total is fixed at 1.5 million BETA.
- As a consequence of the hard cap, the contributors, George and Harry will receive at least 7, 1, and 2 BETA per STEEM contributed (respectively).

This example is chosen to demonstrate how the ratios work.  It is not a realistic example, as most ICO's
will choose to either set `min_unit_ratio = max_unit_ratio` like ALPHA, or choose to use a large `max_unit_ratio` like
BETA.

```
[
 [
  "smt_setup",
  {
   "control_account" : "beta",
   "decimal_places" : 4,
   "max_supply" : "1000000000000000",
   "initial_generation_policy" : [0,
    {
     "pre_soft_cap_unit" : {
      "steem_unit" : [["fred", 3], ["george", 2]],
      "token_unit" : [["$from", 7], ["george", 1], ["henry", 2]]
     },
     "post_soft_cap_unit" : {
      "steem_unit" : [],
      "token_unit" : []
     },
     "min_steem_units_commitment" : {
      "lower_bound" : 5000000,
      "upper_bound" : 5000000,
      "hash" : "dff2e4aed5cd054439e045e1216722aa8c4758b22df0a4b0251d6f16d58e0f3b"
     },
     "hard_cap_steem_units_commitment" : {
      "lower_bound" : 30000000,
      "upper_bound" : 30000000,
      "hash" : "f8e6ab0e8f2c06a9d94881fdf370f0849b4c7864f62242040c88ac82ce5e40d6"
     },
     "soft_cap_percent" : 10000,
     "min_unit_ratio" : 50,
     "max_unit_ratio" : 100,
     "extensions" : []
    }
   ],
   "generation_begin_time" : "2017-06-01T00:00:00",
   "generation_end_time" : "2017-06-30T00:00:00",
   "announced_launch_time" : "2017-07-01T00:00:00",
   "smt_creation_fee" : "1000.000 SBD",
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "beta",
   "cap" : { "amount" : 5000000, "nonce" : "0" },
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "beta",
   "cap" : { "amount" : 30000000, "nonce" : "0" },
   "extensions" : []
  }
 ]
]
```

[This spreadsheet](ico-parameters.ods) will make the relationship clear.

#### GAMMA

The GAMMA token is like BETA, but with one difference:  The
large `max_unit_ratio` means that the maximum issue of 1.5 million
tokens is reached very early in the ICO.  This ICO effectively
divides 1.5 million GAMMA tokens between contributors (provided at least
5 STEEM is contributed).

```
[
 [
  "smt_setup",
  {
   "control_account" : "gamma",
   "decimal_places" : 4,
   "max_supply" : "1000000000000000",
   "initial_generation_policy" : [0,
    {
     "pre_soft_cap_unit" : {
      "steem_unit" : [["fred", 3], ["george", 2]],
      "token_unit" : [["$from", 7], ["george", 1], ["henry", 2]]
     },
     "post_soft_cap_unit" : {
      "steem_unit" : [],
      "token_unit" : []
     },
     "min_steem_units_commitment" : {
      "lower_bound" : 5000000,
      "upper_bound" : 5000000,
      "hash" : "dff2e4aed5cd054439e045e1216722aa8c4758b22df0a4b0251d6f16d58e0f3b"
     },
     "hard_cap_steem_units_commitment" : {
      "lower_bound" : 30000000,
      "upper_bound" : 30000000,
      "hash" : "f8e6ab0e8f2c06a9d94881fdf370f0849b4c7864f62242040c88ac82ce5e40d6"
     },
     "soft_cap_percent" : 10000,
     "min_unit_ratio" : 50,
     "max_unit_ratio" : 300000,
     "extensions" : []
    }
   ],
   "generation_begin_time" : "2017-06-01T00:00:00",
   "generation_end_time" : "2017-06-30T00:00:00",
   "announced_launch_time" : "2017-07-01T00:00:00",
   "smt_creation_fee" : "1000.000 SBD",
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "gamma",
   "cap" : { "amount" : 5000000, "nonce" : "0" },
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "gamma",
   "cap" : { "amount" : 30000000, "nonce" : "0" },
   "extensions" : []
  }
 ]
]
```

#### DELTA

In this ICO we have one million DELTA tokens created
for the founder, and none for contributors.  A modest
contribution of 0.1 STEEM can be made by any user
(including the founder themselves) to trigger the
generation.

```
[
 [
  "smt_setup",
  {
   "control_account" : "delta",
   "decimal_places" : 5,
   "max_supply" : "1000000000000000",
   "initial_generation_policy" : [0,
    {
     "pre_soft_cap_unit" : {
      "steem_unit" : [["founder", 1]],
      "token_unit" : [["founder", 10000]]
     },
     "post_soft_cap_unit" : {
      "steem_unit" : [],
      "token_unit" : []
     },
     "min_steem_units_commitment" : {
      "lower_bound" : 10000000,
      "upper_bound" : 10000000,
      "hash" : "4e12522945b8cc2d87d54debd9563a1bb6461f1b1fa1c31876afe3514e9a1511"
     },
     "hard_cap_steem_units_commitment" : {
      "lower_bound" : 10000000,
      "upper_bound" : 10000000,
      "hash" : "4e12522945b8cc2d87d54debd9563a1bb6461f1b1fa1c31876afe3514e9a1511"
     },
     "soft_cap_percent" : 10000,
     "min_unit_ratio" : 1000,
     "max_unit_ratio" : 1000,
     "extensions" : []
    }
   ],
   "generation_begin_time" : "2017-06-01T00:00:00",
   "generation_end_time" : "2017-06-30T00:00:00",
   "announced_launch_time" : "2017-07-01T00:00:00",
   "smt_creation_fee" : "1000.000 SBD",
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "delta",
   "cap" : { "amount" : 10000000, "nonce" : "0" },
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "delta",
   "cap" : { "amount" : 10000000,  "nonce" : "0" },
   "extensions" : []
  }
 ]
]
```

#### Vesting contributions

It is possible to send part or all of contributions
to a vesting balance, instead of permitting immediate
liquidity.  This example puts 95% in vesting.

```
"token_unit"           : [["$from.vesting", 95], ["$from", 5]]
```

#### Burning contributed STEEM

In this ICO, the STEEM is permanently destroyed rather than going into the wallet of any person.
This mimics the structure of the Counterparty ICO.

```
{
 "steem_unit" : [["null", 1]],
 "token_unit" : [["$from", 1]]
}
```

#### Vesting as cost

In this ICO, you don't send STEEM to the issuer in exchange for tokens.  Instead, you vest STEEM (to yourself),
and tokens are issued to you equal to the STEEM you vested.

```
{
 "steem_unit" : [["$from.vesting", 1]],
 "token_unit" : [["$from", 1]]
}
```

#### Non-STEEM & Hybrid ICO's

ICO's using non-STEEM contributions -- for example, SBD, BTC, ETH, etc. --
cannot be done fully automatically on-chain.   However, such ICO's can be
managed by manually transferring some founder account's distribution to
buyers' Steem accounts in proportion to their non-STEEM contribution.

### Inflation Parameters

Creation of SMT after launch is called *inflation*.

Inflation is the means by which the SMT rewards contributors for
the value they provide.

Inflation events use the following data structure:

```
struct smt_inflation_unit
{
   flat_map< account_name_type, uint16_t >        token_unit;
};

// Event:  Support issuing tokens to target at time
struct token_inflation_event
{
   timestamp           schedule_time;
   smt_inflation_unit  unit;
   uint32_t            num_units;
};
```

This event prints `num_units` units of the SMT token.

#### Possible inflation target

The target is the entity to which the inflation is directed.  The target
may be a normal Steem account controlled by an individual founder, or a
multisig of several founders.

In addition, several special targets are possible representing trustless
functions provided by the blockchain itself:

- Rewards.  A special destination representing the token's posting / voting rewards.
- Vesting.  A special destination representing the tokens backing vested tokens.

#### Event sequences

Traditionally blockchains compute inflation on a per-block basis,
as block production rewards are the main (often, only) means of
inflation.

However, there is no good reason to couple inflation to block
production for SMT's.  In fact, SMT's have no block rewards,
since they have no blocks (the underlying functionality of block
production being supplied by the Steem witnesses, who are
rewarded with Steem).

Repeating inflation at regular intervals can be enabled by
adding `interval_seconds` and `interval_count` to the
`token_inflation_event` data structure.  The result is a new
data structure called `token_inflation_event_seq_v1`:

```
// Event seq v1:  Support repeatedly issuing tokens to target at time
struct token_inflation_event_seq_v1
{
   timestamp           schedule_time;
   smt_inflation_unit  unit;
   asset               new_smt;

   int32_t             interval_seconds;
   uint32_t            interval_count;
};
```

The data structure represents a token inflation event
that repeats every `interval_seconds` seconds, for
`interval_count` times.  The maximum integer value
`0xFFFFFFFF` is a special sentinel value that represents
an event sequence that repeats forever.

Note, the `new_smt` is a quantity of SMT, not a number
of units.  The number of units is determined by dividing
`new_smt` by the sum of `unit` members.

#### Adding relative inflation

Often, inflation schedules are expressed using percentage
of supply, rather than in absolute terms:

```
// Event seq v2:  v1 + allow relative amount of tokens
struct token_inflation_event_seq_v2
{
   timestamp           schedule_time;
   smt_inflation_unit  unit;
   uint32_t            num_units;

   int32_t             interval_seconds;
   uint32_t            interval_count;

   asset               abs_amount;
   uint32_t            rel_amount_numerator;
};
```

Then we compute `new_smt` as follows from the supply:

```
rel_amount = (smt_supply * rel_amount_numerator) / SMT_REL_AMOUNT_DENOMINATOR;
new_smt = max( abs_amount, rel_amount );
```

If we set `SMT_REL_AMOUNT_DENOMINATOR` to a power of two, the division
can be optimized to a bit-shift operation.  To gain more dynamic range
from the bits, we can let the shift be variable:

```
// Event seq v3:  v2 + specify shift in struct
struct token_inflation_event_seq_v3
{
   timestamp           schedule_time;
   smt_inflation_unit  unit;

   int32_t             interval_seconds;
   uint32_t            interval_count;

   asset               abs_amount;
   uint32_t            rel_amount_numerator;
   uint8_t             rel_amount_denom_bits;
};
```

Then the computation becomes:

```
rel_amount = (smt_supply * rel_amount_numerator) >> rel_amount_denom_bits;
new_smt = max( abs_amount, rel_amount );
```

Of course, the implementation of these computations must carefully handle
potential overflow in the intermediate value `smt_supply * rel_amount_numerator`!

#### Adding time modulation

Time modulation allows implementing an inflation rate which changes continuously
over time according to a piecewise linear function.  This can be achieved by simply
specifying the left/right endpoints of a time interval, and specifying absolute amounts
at both endpoints:

```
// Event seq v4:  v3 + modulation over time
struct token_inflation_event_seq_v4
{
   timestamp           schedule_time;
   smt_inflation_unit  unit;

   int32_t             interval_seconds;
   uint32_t            interval_count;

   timestamp           lep_time;
   timestamp           rep_time;

   asset               lep_abs_amount;
   asset               rep_abs_amount;
   uint32_t            lep_rel_amount_numerator;
   uint32_t            rep_rel_amount_numerator;

   uint8_t             rel_amount_denom_bits;
};
```

Some notes about this:

- Only the numerator of relative amounts is interpolated,
the denominator is the same for both endpoints.

- For times before the left endpoint time, the amount at
the left endpoint time is used.

- For times after the right endpoint time, the amount at
the right endpoint time is used.

Code looks something like this:

```
if( now <= lep_time )
{
   abs_amount = lep_abs_amount;
   rel_amount_numerator = lep_rel_amount_numerator;
}
else if( now >= rep_time )
{
   abs_amount = rep_abs_amount;
   rel_amount_numerator = rep_rel_amount_numerator;
}
else
{
   // t is a number between 0.0 and 1.0
   // this calculation will need to be implemented
   // slightly re-arranged so it uses all integer math

   t = (now - lep_time) / (rep_time - lep_time)
   abs_amount = lep_abs_amount * (1-t) + rep_abs_amount * t;
   rel_amount_numerator = lep_rel_amount_numerator * (1-t) + rep_rel_amount_numerator * t;
}
```

#### Inflation operations

The inflation operation is specified as follows:

```
struct smt_setup_inflation_operation
{
   account_name_type   control_account;

   timestamp           schedule_time;
   smt_inflation_unit  inflation_unit;

   int32_t             interval_seconds = 0;
   uint32_t            interval_count = 0;

   timestamp           lep_time;
   timestamp           rep_time;

   asset               lep_abs_amount;
   asset               rep_abs_amount;
   uint32_t            lep_rel_amount_numerator = 0;
   uint32_t            rep_rel_amount_numerator = 0;

   uint8_t             rel_amount_denom_bits = 0;

   extensions_type     extensions
};
```

The `setup_inflation_operation` is a *pre-setup* operation which must be executed *before*
the `smt_setup_operation`.   See the section on pre-setup operations.

#### Inflation FAQ

- Q:  Can the SMT inflation data structures express Steem's [current inflation scheme](https://github.com/steemit/steem/issues/551)?
- A:  Yes (except for rounding errors).
- Q:  Can the SMT inflation data structures reward founders directly after X months/years?
- A:  Yes.
- Q:  I don't care about time modulation.  Can I disable it?
- A:  Yes, just set the `lep_abs_amount == rep_abs_amount` and `lep_rel_amount_numerator == rep_rel_amount_numerator` to the same value, and set `lep_time = rep_time` (any value will do).
- Q:  Can some of this complexity be hidden by a well-designed UI?
- A:  Yes.
- Q:  Can we model the inflation as a function of time with complete accuracy?
- A:  The inflation data structures can be fully modeled / simulated.  For some issue structures, the amount issued depends on how much is raised, so the issue structures cannot be modeled with complete accuracy.

TODO:  Make some pretty graphs
TODO:  Examples:  Steem old inflation scheme, Steem new inflation scheme, Bitcoin, send % to founders, send % to founders after time

### Named token parameters

Some behaviors of STEEM are influenced by compile-time configuration constants which are implemented by `#define`
statements in the `steemd` C++ source code.  It makes sense for the equivalent behaviors for SMT's to be
configurable by the SMT creator.

These parameters are `runtime_parameters` and `setup_parameters`.  The `setup_parameters` are a field in
`smt_setup_operation`; they must be set before `smt_setup_operation` and cannot be changed once
`smt_setup_operation` is executed.  The `runtime_parameters` are a field in
`smt_set_runtime_parameters_operation`, they can be changed by the token creator at any time.

These operations are defined as follows:

```
struct smt_set_setup_parameters_operation
{
   account_name_type                                 control_account;

   flat_set< smt_setup_parameter >                   setup_parameters;
   extensions_type                                   extensions;
};

struct smt_set_runtime_parameters_operation
{
   account_name_type                                 control_account;

   flat_set< smt_runtime_parameter >                 runtime_parameters;
   extensions_type                                   extensions;
};
```

Currently the following `setup_parameters` and `runtime_parameters` are defined:

```
struct smt_param_allow_vesting                    { bool value = true;  };
struct smt_param_allow_voting                     { bool value = true;  };

typedef static_variant<
   smt_param_allow_vesting,
   smt_param_allow_voting
   > smt_setup_parameter;

struct smt_param_windows_v1
{
   uint32_t cashout_window_seconds = 0;                // STEEM_CASHOUT_WINDOW_SECONDS
   uint32_t reverse_auction_window_seconds = 0;        // STEEM_REVERSE_AUCTION_WINDOW_SECONDS
};

struct smt_param_vote_regeneration_period_seconds_v1
{
   uint32_t vote_regeneration_period_seconds = 0;      // STEEM_VOTE_REGENERATION_SECONDS
   uint32_t votes_per_regeneration_period = 0;
};

struct smt_param_rewards_v1
{
   uint128_t               content_constant = 0;
   uint16_t                percent_curation_rewards = 0;
   uint16_t                percent_content_rewards = 0;
   curve_id                author_reward_curve;
   curve_id                curation_reward_curve;
};

typedef static_variant<
   smt_param_windows_v1,
   smt_param_vote_regeneration_period_seconds_v1,
   smt_param_rewards_v1
   > smt_runtime_parameter;
```

UI's which allow inspecting or setting these parameters should be aware of
the type and scale of each parameter.  In particular, percentage parameters
are on a basis point scale (i.e. 100% corresponds to a value of
`STEEMIT_100_PERCENT = 10000`), and UI's or other tools for creating or
inspecting transactions *must* use the basis point scale.

## Parameter constraints

Several dynamic parameters must be constrained to prevent abuse scenarios that could harm token users.

- `0 < vote_regeneration_seconds < SMT_VESTING_WITHDRAW_INTERVAL_SECONDS`
- `0 <= reverse_auction_window_seconds + SMT_UPVOTE_LOCKOUT < cashout_window_seconds < SMT_VESTING_WITHDRAW_INTERVAL_SECONDS`

## SMT vesting semantics

SMT's have similar vesting (powerup / powerdown) semantics to STEEM.  In particular:

- SMT's can be "powered up" into a vesting balance
- SMT's in a vesting balance can be "powered down" over 13 weeks
(controlled by hardcoded `SMT_VESTING_WITHDRAW_INTERVALS`, `SMT_VESTING_WITHDRAW_INTERVAL_SECONDS` parameters)
- Voting is affected only by powered-up tokens
- Vesting balance cannot be transferred or sold

Additionally, some token inflation may be directed to vesting balances.  These newly "printed"
tokens are effectively split among all users with vesting balances proportional to the number of tokens
they have vested.  As the number of tokens printed is independent
of users' vesting balances, the percentage rate of return this represents will vary
depending on how many tokens are vested at a time.

## Content rewards

Tokens flow from SMT inflation into the reward fund.  The blockchain uses algorithms
to decide:

- (1) How to divide the token-wide rewards among posts
- (2) How to divide rewards within a post among the author and curators (upvoters) of that post

The algorithms to solve these problems operate as follows:

- (1) Posts are weighed *against other posts* according to the *reward curve* or `rc`.
- (2a) The curators collectively receive a fixed percentage of the post, specified by the `curation_pct` parameter.
- (2b) The author receives the remainder (after applying any beneficiaries or limited/declined author reward).
- (2c) Curators are weighted *against other curators of that post* according to the *curation curve* or `cc`.

![creation.png](img/creation.png)

## Curve definitions

The reward curve can be *linear* or *quadratic*.  The linear reward curve `rc(r) = r` passes the R-shares
(upvotes) through unchanged.  The quadratic reward curve `rc(r) = r^2 + 2rs` has increasing slope.

For an illustration of the meaning of reward curves, imagine grouping the most-upvoted posts as follows:

- Section A consists of the top 10% of posts by upvotes.
- Section B consists of the next 10% of posts by upvotes.

Here's how the rewards differ:

- With either reward curve, Section A posts will have greater rewards than Section B posts since they have more upvotes.
- With the quadratic reward curve, Section A posts will have an *additional boost* relative to Section B posts, since Section A posts will get *more rewards per upvote*.
- With the linear reward curve, Section A and Section B will get the same reward per upvote.

Possible curation curves are:

- Linear `cc(r) = r`
- Square-root `cc(r) = sqrt(r)`
- Bounded `cc(r) = r / (r + 2s)`.

To help visualize, here are some plots called *pie charts*.  Each colored area
represents how curation rewards are divided among curators with equal voting power.

![Reward curves and curation curves](img/rc-cc.png)

- The rectangular vertical column shows the immediate reward upon making an upvote.
- The colored area extending to the right shows how the rewards of a curator grow as later curators vote.
- When both curves are linear, everyone gets the same curation reward regardless of which post they vote on.
- In the case of `rc_linear + cc_sqrt` and `rc_quadratic + cc_bounded`, the same height rectangles mean everyone gets about the same initial curation reward, call this `ICR=`.
- In the case of `rc_linear + cc_bounded`, the rectangles are decreasing in height.  This represents a progressive *handicap* against voting for already-popular posts, call this `ICR-`.
- In the case of `rc_quadratic + cc_sqrt` and `rc_quadratic + cc_linear`, the rectangles are increasing in height.  Call this `ICR+`.

Fundamentally, curation is making a prediction that upvotes will occur in the future.  As reward system designers, our criterion for selecting a curve
should be to reward successful predictions.  Which curve satisfies this criterion depends on the relationship between current and future upvotes.

- If a post's future upvotes are *independent* of its current upvotes, we should choose an `ICR=` curve.
- If a post's future upvotes are *positively correlated* with its current upvotes, we should choose some `ICR-` curve, ideally somehow tuned to the amount of correlation.
- If a post's future upvotes are *negatively correlated* with its current upvotes, we should choose some `ICR+` curve, ideally somehow tuned to the amount of correlation.

In practice, independence or a modest positive correlation should be expected, so an `ICR=` or `ICR-` curve should be chosen.
For STEEM itself, curation was originally the quadratic `ICR=`, as of hardfork 0.19 it is the linear `ICR=`.

## Target votes per day

Each account has a `voting_power`, which is essentially a "mana bar" that fills from 0% to 100% over time at a constant rate.
That rate is determined by two parameters:

- (a) The time it takes to regenerate the bar to 100%, `vote_regeneration_period_seconds`
- (b) The `voting_power` used by a maximum-strength vote

The `vote_regeneration_period_seconds` is specified directly.  For (b), instead of
specifying the voting power of a maximum-strength vote directly, instead you specify
`votes_per_regeneration_period`.  Then the maximum-strength vote is set such that a
user casting that many max-strength votes will exactly cancel the regeneration.

## Votability and Rewardability

In this section, we introduce the concepts of *votability* and *rewardability*.

- A token is *votable* for a comment if the balance of that token influences the comment.
- For a given vote, each votable token of the comment is either *rewardable* or *advisory*.
- If a token is rewardable, then the vote affects the comment's reward in that token.
- If a token is advisory, then the vote does not affect the comment's reward in that token.

Advisory votes do not affect rewards or voting power.  However, the ranking algorithms and
estimated reward calculations still apply advisory votes, so UI's may display advisory posts
accordingly.

The votable token set is determined by `allowed_vote_assets` which is a `comment_options_extension`.

```
struct allowed_vote_assets
{
   flat_map< account_name_type, votable_asset_info >      votable_assets;
};

struct votable_asset_info_v1
{
   share_type        max_accepted_payout    = 0;
   bool              allow_curation_rewards = false;
};

typedef static_variant< votable_asset_info_v1 >           votable_asset_info;
```

The following rules are applied to determine whether tokens are votable:

- STEEM is votable for every post.
- A token is votable for a post if it appears in the post's `votable_assets`.
- Otherwise, the token is not votable for this post.

And these are the rules for whether a token is rewardable:

- In order to be rewardable for a post, a token must be votable for that post.
- If, for some post/token, that post's `max_accepted_payout` of the token is zero,
then the token is not rewardable for that post.
- If some voter (i.e. upvoter / downvoter) has a zero balance of a token, then that token
is not rewardable for that voter's votes.
- If the `max_accepted_payout` for any non-STEEM token is nonzero, then the
`max_accepted_payout` for STEEM/SBD must be at least the default `max_accepted_payout`.

Implementation notes:

- For an advisory vote, all rewards are zero, including curators and beneficiaries.  This is
because the blockchain applies the `max_accepted_payout` cap before the curator / beneficiary
computations.
- Currently (as of hardfork 0.19), the Steem blockchain *does* deduct voting power for advisory
Steem votes.  This behavior will be changed in a future hardfork (Steem issue #1380).
- At most two tokens may be specified in `votable_assets`.  This means each post is voted
with at most three tokens (including STEEM).
- The default `max_accepted_payout` is stored in `max_accepted_steem_payout_latch` member
of `dynamic_global_properties_object`.  Clients should populate `max_accepted_payout` of
a post based on this member, in case the default value changes in a future version.

No consensus level restriction forces any particular post to have any particular
`allowed_vote_assets`.  As a consequence, any post may mark itself as eligible to
be rewarded in any token.  However, UI's may impose their own non-consensus validation
rules on `allowed_vote_assets`, and hide posts that violate these non-consensus
validation rules.

For example, in a Hivemind community with a corresponding token, there may be a
validation rule that the `allowed_vote_assets` specified in each post in that
Hivemind community must include the token of that community.  This is a
non-consensus validation rule, since the entire concept of a post existing in
a Hivemind community is a non-consensus concept.  Since it is a non-consensus
validation rule, no consensus logic can enforce it.  However, UI's that are
aware of Hivemind communities may refuse to index or display posts that violate
this validation rule.

## Hardcoded Token Parameters

Hardcoded parameters are configuration constants that affect the behavior of
SMT's, but are deliberately excluded from `smt_setup_parameters` or
`smt_runtime_parameters`.  The reason they are designed to be non-configurable
is that allowing these parameters to significantly deviate from the values
used for STEEM results in significant risks, such as:

- May result in a very complicated implementation
- May result in extreme end-user frustration
- May threaten the security and stability of the token
- May threaten the security and stability of STEEM

Here is the list of such hardcoded parameters:

- `SMT_UPVOTE_LOCKOUT_HF17` : Hardcoded -- This value locks out upvotes from posts at a certain time prior to "CASH OUT" to prevent downvote abuse immediately prior to "CASH OUT."
- `SMT_VESTING_WITHDRAW_INTERVALS` : Hardcoded
- `SMT_VESTING_WITHDRAW_INTERVAL_SECONDS` : Hardcoded
- `SMT_MAX_WITHDRAW_ROUTES` : Hardcoded
- `SMT_SAVINGS_WITHDRAW_TIME` : Hardcoded
- `SMT_SAVINGS_WITHDRAW_REQUEST_LIMIT` : Hardcoded
- `SMT_MAX_VOTE_CHANGES` : Hardcoded
- `SMT_MIN_VOTE_INTERVAL_SEC` : Hardcoded
- `SMT_MIN_ROOT_COMMENT_INTERVAL` : Hardcoded
- `SMT_MIN_REPLY_INTERVAL` : Hardcoded
- `SMT_MAX_COMMENT_DEPTH` : Hardcoded
- `SMT_SOFT_MAX_COMMENT_DEPTH` : Hardcoded
- `SMT_MIN_PERMLINK_LENGTH` : Hardcoded
- `SMT_MAX_PERMLINK_LENGTH` : Hardcoded

## Mandatory token parameters

The token parameters set by `smt_setup_parameters` or
`smt_runtime_parameters` have default values.  A few STEEM-equivalent parameters
are specified by `smt_setup_operation` fields, these are the parameters which
do not have a default value, and thus, must be specified for every asset.

- `SMT_MAX_SHARE_SUPPLY` : Set by `smt_setup_operation.max_supply`
- `SMT_BLOCKCHAIN_PRECISION` : Set by `pow(10, smt_setup_operation.decimal_places)`
- `SMT_BLOCKCHAIN_PRECISION_DIGITS` : Set by `smt_setup_operation.decimal_places`

### Arbitrary Reward Splitting

All Steem based interfaces have the option of splitting token rewards among a set of arbitrary recipients, which could include an interface, community manager, referrer and more.  An interface can also provide this optionality to the author. Add to this.

## SMT interaction with existing operations

- `comment_payout_beneficiaries` : The existing `comment_payout_beneficiaries` will only redirect STEEM.  In the future, `comment_payout_beneficiaries` functionality which allows redirecting SMT rewards may be added.
- `comment_options` : `max_accepted_payout`, `allow_votes` only affects STEEM, see [here](#votability-and-rewardability) to restrict `max_accepted_payout` for assets.  `allow_curation_rewards` affects all tokens.
- `vote_operation` : Multiple tokens in the comment's votable set vote.
- `transfer_operation` : Supports all SMT's.
- Escrow operations:  Do not support SMT's.
- `transfer_to_vesting_operation` : Supports all SMT's that support vesting.
- `withdraw_vesting_operation` : Supports all SMT's that support vesting.
- `set_withdraw_vesting_route_operation` : Does not support SMT's.
- `account_witness_vote_operation` : SMT's do not affect witness votes.
- `account_witness_proxy_operation` : SMT's do not affect witness votes.
- `feed_publish_operation` : Feeds may not be published for SMT's.
- `convert_operation` : SMT's cannot be converted.
- Limit order operations : Limit orders are fully supported by SMT's trading against STEEM.
- `transfer_to_savings_operation` : SMT's support savings.
- `decline_voting_rights_operation` : Affects SMT votes as well as STEEM votes.
- `claim_reward_balance_operation` : Restrictions on this operation are relaxed to allow any asset in any of the three fields, including SMT's.
- `delegate_vesting_shares_operation` : Supports all SMT's that support vesting.

# Costless SMT Operations And Bandwidth Rate Limiting

Like STEEM, SMTs can be transferred across Steem at zero cost. Steem enables this due to bandwidth rate limiting based on percentage of stake in the network, which means the blockchain calculates how much STEEM an account has temporaily vested to determine how much bandwidth the account is permitted for transfers, posting and other operations across a period of time. In a future version of Steem, possesion of an account name could permit some small degree of bandwidth to allow for even greater user experience.

## Demand for Steem 

Because users need to increasingly hold STEEM in order to participate at a rate commensurate with their growing potentials in respective SMT ecosystems, there is growing demand for users to hold STEEM. At an application level, the demand for bandwidth may be satisfied by users or by businesses, which can delegate surplus bandwidth to their users.  At a platform level, other cause for demand may include exclusive financing opportunities, increased rate of holding due to market maker reserve ratios and growing attention to the base currency.

## Fee-less Operations Necessary for Quality User Experience

SMTs represent best in class tokens for content for several reasons highlighted throughout this paper, but perhaps the most point-blank reason comes from the fee structure.  Because of bandiwdth rate limiting, Steem may never charge applications or users transaction fees for basic operations such as voting, posting and transferring.  This lack of fees allows Steem based apps to compete with their non-blockchain counterparts, such as Facebook or Reddit, which certainly do not charge fees for actions such as 'Like' and 'Upvote'.  If these applications did charge fees they would become far less used and could be more easily competed against.

# Decentralized Exchange
One of the valuable features of SMTs is their immediate access to functioning, unmanned markets against the liquid asset, STEEM.

## Automatic Order Matching
The Decentralized Exchange (DEX) structures of Steem allow assets to automatically be matched for best possible price when bids and asks overlap, unlike other DEXs which require a "man in the middle" or user-agent, to match orders.  Automatic, rather than middle-man-faciliated order matching is important for security of Steem-based assets and for the replicability and safety of DEX interfaces.

## Diverse Asset Types
There are several assets that SMT users and creators will have access to by way of the Steem DEX: STEEM; SBD; SMTs; Simple Derivatives (IOUs).  These neighboring assets can increase the visibility and network effect of all created SMTs.

STEEM is the gateway token for assets issued on Steem, staying relevant by acting as the bandwidth usage measuring stick across Steem's meta-assets.  STEEM is also the common denominator asset, acting as a trading pair for all of Steem's meta-assets.

SBD (Steem Blockchain Dollars) are an experimental asset on Steem that relate to the US Dollar originating back to Steem's launch in 2016. It is unclear if SBD will bring value to holders of USD as they will compete, possibly poorly, with IOU USDs, however, SBDs will bring value to speculators.

SMTs as described in this proposal are an important part of growing the token ecosystem and bringing crypto assets to the mainstream.  SMTs will trade against STEEM across the DEX.

Simple Derivatives (IOUs) will be possible via SMT issuance.  For instance, if an SMT is issued without inflation or rewards pool properties, then the issuer can reliably back the token with another real world asset such as bitcoin or USD.  In this instance, the issuer could create business as a gateway by trading their IOU for btc or USD.  Users would buy the IOU to gain access to the Steem DEX. This market would add diversity and value flow to the Steem ecosystem while adding to the DEX's network effect.

## Zero Trading and Transfer Fees
The Steem DEX is the first DEX to exist without trading fees, to the benefit of SMT creators and traders alike.  This is made possible by bandwidth rate limiting, a concept first introduced in the [original Steem White Paper](https://steem.io/SteemWhitePaper.pdf).

# Ecosystem Support

## Integrating SMTs into Websites and Apps

### APIs and Documentation

To be continously updated for SMTs.  Current *STEEM* APIs exist here: http://steem.readthedocs.io/en/latest/index.html and https://steemit.github.io/steemit-docs/

### Shared Tools for Signup, Key Signing and Wallet Functions

Several shared tools exist to support applications that wish to outsource signup, transaction signing and wallet functions, such as SteemConnect (Add link to SteemConnect launch post).

# Conclusion

Through a combination of open asset-issuance, bandiwdth rate limiting as transaction costs, permanent-availability of content, real-time transaction speeds, autonomous distribution of tokens, decentralized exchange, automated market making and ICO contracts, Steem offers the premier token protocol for publishers across the internet.  

# References

[1] Steemit, Inc. Scott, et al. Steem Whitepaper 2.0. A protocol for bringing smart, social currency to publishers and content businesses across the internet. (https://www.steem.io/steem-whitepaper-2-0)

[2] Eyal Hertzog, Guy Benartzi & Galia Benartzi. Bancor Protocol. Continuous Liquidity and Asynchronous Price
Discovery for Tokens through their Smart Contracts. (https://www.bancor.network/static/bancor_protocol_whitepaper_en.pdf)

# Appendix

## Implementation Notes

## Unit Tests
