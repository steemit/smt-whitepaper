CONFIDENTIAL AND PRIVILEGED; DO NOT SHARE
Proposal by Steemit Inc
Copyright (c) Steemit, Inc. 2017
Status: DRAFT

# Smart Media Tokens 

Steem Proposal: A Token Protocol for Achieving Autonomous Application Growth and Fundraising 

- [Introduction](#introduction)
- [Owner's manual](#owners-manual)
  - [Establish a Name Space](#establish-a-name-space)
    - [Token consensus](#token-consensus)
  - [Token Generation and Initialized Parameters](#token-generation-and-initialized-parameters)
    - [Creation fee](#creation-fee)
    - [Descriptor](#descriptor)
    - [Structuring Token Generation Events and Initial Token Offerings (TGEs and ITOs)](#structuring-token-generation-events-and-initial-token-offerings-tges-and-itos)
      - [Why unit ratios?](#why-unit-ratios)
      - [UI treatment of unit ratios](#ui-treatment-of-unit-ratios)
      - [Defining SMT distribution](#defining-smt-distribution)
        - [Special account names](#special-account-names)
      - [Defining SMT issue policy](#defining-smt-issue-policy)
      - [Ratios](#ratios)
      - [Caps](#caps)
      - [Hidden cap FAQ](#hidden-cap-faq)
      - [Launch](#launch)
      - [Examples](#examples)
        - [Full JSON example](#full-json-example)
        - [Single-segment with min and cap](#single-segment-with-min-and-cap)
        - [Fixed-float no-reserve](#fixed-float-no-reserve)
        - [Vesting contributions](#vesting-contributions)
        - [Burning contributed STEEM](#burning-contributed-steem)
        - [Vesting as cost](#vesting-as-cost)
        - [Non-STEEM & Hybrid ITO's](#non-steem--hybrid-itos)
      - [Market maker accounts](#market-maker-accounts)
    - [Inflation Parameters](#inflation-parameters)
      - [Possible inflation target](#possible-inflation-target)
      - [Event sequences](#event-sequences)
      - [Adding relative inflation](#adding-relative-inflation)
      - [Adding time modulation](#adding-time-modulation)
      - [Inflation operations](#inflation-operations)
      - [Inflation FAQ](#inflation-faq)
    - [Token Precision Parameters](#token-precision-parameters)
  - [Reward curves](#reward-curves)
  - [Target votes per day](#target-votes-per-day)
  - [Regeneration time](#regeneration-time)
  - [Dynamic Rewards Parameters](#dynamic-rewards-parameters)
    - [Parameter Constraints](#parameter-constraints)
  - [Hardcoded Token Parameters](#hardcoded-token-parameters)
  - [SMT Parameters Commentary](#smt-parameters-commentary)
- [Decentralized Exchange](#decentralized-exchange)
  - [Decentralized Order Matching](#decentralized-order-matching)
  - [Diverse Asset Types](#diverse-asset-types)
  - [ZERO Trading Fees](#zero-trading-fees)
- [Ecosystem Support](#ecosystem-support)
- [Conclusion](#conclusion)

- Github: https://github.com/steemit/smt-whitepaper/blob/collab/smt-manual/manual.md
- Git Changes: https://github.com/steemit/smt-whitepaper/commit/6eab36d3b941f52f65e78f3be72efdd5bf5afc2e

# Introduction

Smart Media Tokens (SMTs) is a proposal to build a protocol on the Steem Blockchain that allows for meta-assets powered by STEEM as their bandwidth calculation token.  Inspired by the revolutionary  properties of the STEEM asset, SMTs will be an upgrade above previous blockchain's meta-asset protocols due to extensive, user-oriented programmability and the Steem ecosystem's tools for integrations at website and application layers.

Smart Media Tokens are an expansion of the successful relationship established between STEEM and the social websites sitting atop of it, such as steemit.com, which has grown to be a top 3000 website in Alexa rankings in less than one year, solely from integrating the incentive model of STEEM.  With SMTs, any website or content library across the internet may have one or more tokens integrated into its interface to facilitate fundraising and autonomous growth.

These tokens are designed to allow website operators flexibility during the integration of the token into their community by choosing from many parameters that may be structured creatively at outset or refined over time.  Any tokens launched as Smart Media Tokens shall benefit from a blockchain ecosystem built with decentralized exchange, and many applications and libraries to support successful deployment, fundraising and growth.

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

TODO:  Add or link to detailed instructions showing how to create
an account with the CLI wallet.

TODO:  Add or link to detailed instructions on how to transfer an account.
For example, if you're buying a desirably named account from somebody,
we should explain:

- How do they send you the account?
- How do you verify you've received the account and take full control of it?
- How can you atomically, trustlessly swap STEEM or SBD for an account?
- What parts of this can be done with the steemit.com, SteemConnect, the mobile wallet, or other official UI's?
- What steps do you need to take to ensure the seller cannot fraudulently use the account recovery process to get the account back after they've sold it?
- In the case of an account with steemit.com as its recovery agent, what information do the buyer and seller need to give us to ensure we would recover the account to the proper party?

TODO:  We should probably recommend to set up another account, or a multisig
of accounts, as the authority on the control account.  However, before we
make this recommendation, we must do testing to be sure the account will
remain functional in at least the CLI wallet, and possibly the steemit.com,
SteemConnect, and/or mobile wallet UI's.

### Token consensus

Since tokens participate in atomic transactions also involving
STEEM, they have been designed as part of the STEEM
blockchain's consensus.

## Token Generation and Initialized Parameters

### Creation fee

TODO:  Explain and justify the blockchain's fee to create an asset

### Descriptor

Each SMT has an associated descriptor object which has
*permanent configuration data*.  This data cannot be changed after launch!
The descriptor is set by the `SMT_setup_operation`:

```
struct smt_setup_operation
{
   account_name_type       control_account;
   uint8_t                 decimal_places = 0;
   int64_t                 max_supply = STEEMIT_MAX_SHARE_SUPPLY;

   smt_distribution        initial_distribution_policy;

   time_point_sec          distribution_end_time;
   time_point_sec          launch_time;

   extensions_type         extensions;
};
```
### Structuring Token Generation Events and Initial Token Offerings (TGEs and ITOs)

SMT token creation exchange takes place in a series of *units*.  To understand units, it's best to start with an example.

ALPHA wants to sell a token to the crowd to raise funds
where 7% of contributed STEEM goes to Founder Account A, 23% of contributed STEEM goes to Founder Account B, and 70% of contributed STEEM goes to Founder Account C.

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

This token-unit contains 6 ALPHA-satoshis, or 0.0006 ALPHA (if ALPHA
has 4 decimal places).

Next we define the *unit ratio* as the relative rate at which `token_unit`
are issued as `steem_unit` are contributed.  So to match the specification
of 6 ALPHA per 1 STEEM, we need to issue 1000 ALPHA-units per STEEM-unit.
Therefore the unit ratio of this crowdsale is 1000.

#### Why unit ratios?

Why does the blockchain use unit ratios, rather than simply specifying
prices?

The answer is that it is possible to write TGE definitions for which
price is ill-defined.  For example:

- `"$from"` does not occur in `token_unit`
- `"$from"` occurs in both `token_unit` and `steem_unit`
- A combination of `"$from"` and `"$from.vesting"` occurs
- Future expansion allows new special accounts

All of these TGE definitions have a unit ratio, but defining a
single quantity to call "price" is complicated or impossible for
TGE's like these.

#### UI treatment of unit ratios

As a consequence of the above, the concept of "TGE price" is purely
a UI-level concept.  UI's which provide a TGE price should do the following:

- Document the precise definition of "price" provided by the UI
- Be well-behaved for pathological input like above
- Have a button for switching between a unit ratio display and price display

#### Defining SMT distribution

The data structure used to define units is:

```
struct smt_generation_unit
{
   flat_map< account_name_type, uint16_t >        steem_unit;
   flat_map< account_name_type, uint16_t >        token_unit;
};
```

##### Special account names

The `token_unit` member allows a special account name, `$from`, which should be illegal to be created, and will represent the contributor.

Also supported is `$from.vesting` which represents the vesting balance of the `$from` account.

#### Defining SMT issue policy

A *segment* is a portion of a SMT.  During the contribution phase of a SMT,
exactly one segment is active at any point in time.  The transition from
one segment to the next is triggered either by passing a specific point in
time, or by exceeding a predefined cap.

SMT issue segments are defined with the following data structure:

```
struct smt_distribution
{
   time_point_sec      end_time;

   smt_generation_unit pre_soft_cap_unit;
   smt_generation_unit post_soft_cap_unit;

   smt_cap_commitment  min_steem_units_commitment;
   smt_cap_commitment  hard_cap_steem_units_commitment;

   uint16_t            soft_cap_percent;

   uint32_t            begin_unit_ratio;
   uint32_t            end_unit_ratio;

   extensions_type     extensions;
};
```

The caps function as follows:

- If fewer than `min_steem_units` are contributed, then the TGE is cancelled and all contributors are fully refunded.
- The soft cap is defiend as `soft_cap_percent` times `hard_cap_steem_units`.
- Before the soft cap is reached, STEEM and tokens are generated according to `pre_soft_cap_unit`.
- After the soft cap is reached, STEEM and tokens are generated according to `post_soft_cap_unit`.

The ratios must be defined with `begin_unit_ratio >= end_unit_ratio > 0`.

#### Ratios

How do `begin_unit_ratio` / `end_unit_ratio` work, and what should they be set to?

If you want a Proportional Generation Event, where N tokens are created for every M STEEM
contributed (and so the total number of tokens generated depends on the total number of STEEM
contributed):

- Set `begin_unit_ratio = end_unit_ratio = 1`
- Set `steem_unit` so that its sum is M
- Set `token_unit` so that its sum is N

If you want a Fixed Generation Event, where some fixed number of tokens T are created,
and divided among contributors:

- Set `begin_unit_ratio` to a very large number such
as 4,000,000,000
- Let N be the sum of `token_unit`
- Set `end_unit_ratio` to `T / (N * hard_cap)`

You can think of the settings as a Bounded Proportional Generation Event:  Use
Proportional Generation until T tokens are created, then use Fixed Generation thereafter,
where `T = N * hard_cap * end_unit_ratio`.

TODO:  Test all this, and double check the math.

#### Caps

A cap is defined as simply an `sha256` digest.  Here are the relevant data structures:

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

Then `sha256( cap )` must match one of the `commitment` fields in the
`smt_distribution` operation.  Additionally, the `amount` must be between
the `lower_bound` and `upper_bound`.

- The UI should provide functionality to immediately reveal the cap.
- The UI should warn the user to WRITE DOWN the amount and nonce.
- The UI should allow the user to set lower and upper bound on the cap.

The UI / wallet should set
`nonce = H(privkey + control_account + lower_bound + upper_bound + current_date)`
to allow the nonce to be recovered from the private key.

#### Hidden cap FAQ

- Q: Should my TGE have a cap?
- A: Some set of people stay away from uncapped TGE's due to perceived "greed",
or want a guaranteed lower bound on the percentage of the TGE their
contribution will buy.  If you want this set of people to participate,
use a cap.

- Q: Should my cap be hidden?
- A: Some people like the transparency and certainty of a public cap.
Other people think a hidden cap creates excitement and builds demand.  One
possible compromise is to publish the previous and next power of 10, for example
"this TGE's cap is between 1 million and 10 million STEEM."

- Q: How do I disable the cap?
- A: Set it so that the cap would occur above `STEEMIT_MAX_SHARE_SUPPLY`.

#### Launch

The *launch time* is the time at which tokens become transferrable,
it occurs sometime after the end of the distribution.

The token cannot launch until the hidden cap and hidden minimum have
been revealed.  If the control account does not publish the hidden cap
for any reason [1], then contributors will be able to request a refund
of their STEEM.

```
struct smt_refund
{
   account_name_type       contributor;
   account_name_type       control_account;

   asset                   amount;

   extensions_type         extensions;
};
```

[1] Possible reasons range from lost key / nonce to malicious intent.

#### Examples

##### Full JSON example

Suppose BETA is defined with the following definitions:

```
[
 ["SMT_setup_operation",
  {
   "control_account"      : "beta",
   "decimal_places"       : 4,
   "max_supply"           : STEEMIT_MAX_SHARE_SUPPLY,
   "launch_time"          : "2017-06-01T00:00:00"
  },
 ],
 ["SMT_define_unit_operation",
  {
   "control_account"      : "beta",
   "unit_num"             : 1001,
   "steem_unit"           : [
    ["founder_a",  7],
    ["founder_b", 23],
    ["founder_c", 70]
   ],
   "token_unit"           : [
   ["$from", 5],
   ["founder_d", 1]
   ]
  },
 ],
 ["SMT_define_segment_operation",
  {
   "control_account"      : "beta",
   "end_time"             : "2017-07-01T00:00:00",
   "unit_num"             : 1001,
   "min_steem_units"      : 1000000,
   "max_steem_units"      : 30000000,
   "begin_unit_ratio"     : 1000,
   "end_unit_ratio"       : 600
  }
 ]
]
```

From this data structure we get the following information:

- This crowdsale will occur for the month of June, 2017.
- Each STEEM unit is 100 STEEM-satoshis, or 0.1 STEEM.
- Each BETA unit is 6 BETA-satoshis, or 0.0006 BETA.
- The minimum raised is 1 million STEEM-units, or 100,000 STEEM.
- The maximum raised is 30 million STEEM-units, or 3 million STEEM.
- The maximum BETA created is 30 million * 600 = 18 billion BETA units.
- At 0.006 BETA per unit, 18 billion BETA units is 10.8 million BETA.
- Initially, BETA will be created at a rate of 1000 BETA units per STEEM unit.

This spreadsheet will make the relationship clear.

TODO:  Add screenshot
TODO:  Add link to spreadsheet file

##### Single-segment with min and cap

This is an example where 1 STEEM for 1 token,
100,000 STEEM minimum, 7 million maximum.

Note that, for a token with 2 decimal places,
we must issue 1 token-satoshis for every
10 STEEM-satoshis.  Furthermore, we have
`min_steem_units = 10,000,000` because one
STEEM-unit is 10 satoshis or 0.01 STEEM, so
100,000 STEEM is 10 million STEEM-units.

```
"decimal_places"       : 2
"steem_unit"           : [["founder", 10]]
"token_unit"           : [["$from", 1]]
"min_steem_units"      : 10000000
"max_steem_units"      : 700000000
"begin_unit_ratio"     : 1
"end_unit_ratio"       : 1
```

TODO:  Do billions and billions need to be quoted?
TODO:  Write script to process this into operations
TODO:  Test this

##### Fixed-float no-reserve

This is an example where 1 million tokens
will be issued according to the amount of STEEM received.

```
"decimal_places"       : 3
"steem_unit"           : [["founder", 1000]]
"token_unit"           : [["$from", 1]]
"min_steem_units"      : 0
"max_steem_units"      : 1000000000
"begin_unit_ratio"     : 1000000000
"end_unit_ratio"       : 1
```

In this example, if 1 STEEM is contributed, that
contributor will receive the whole 1 million tokens.
More contributions will lower the ratio, the ratio
can drop as low as 1 STEEM per token-satoshi.

##### Vesting contributions

It is possible to send part or all of contributions
to a vesting balance, instead of permitting immediate
liquidity.  This example puts 95% in vesting.

```
"token_unit"           : [["$from.vesting", 95], ["$from", 5]]
```

##### Burning contributed STEEM

In this ITO, the STEEM is permanently destroyed rather than going into the wallet of any person.
This mimics the structure of the Counterparty ITO.

```
{
 "steem_unit" : [["null", 1]],
 "token_unit" : [["$from", 1]]
}
```

##### Vesting as cost

In this ITO, you don't send STEEM to the issuer in exchange for tokens.  Instead, you vest STEEM (to yourself),
and tokens are issued to you equal to the STEEM you vested.

```
{
 "steem_unit" : [["$from.vesting", 1]],
 "token_unit" : [["$from", 1]]
}
```

##### Non-STEEM & Hybrid ITO's

ITO's using non-STEEM contributions -- for example, SBD, BTC, ETH, etc. -- cannot be done fully automatically on-chain.   However, such ITO's can be managed by manually transferring some founder account's distribution to buyers' Steem accounts in proportion to their non-STEEM contribution.

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
   inflation_target    target;

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

### Token Precision Parameters
These are values that may be set to determine how many digits a token supports. These values may only be set once.

NB, we will change STEEMIT to STEEM in the chain, see [here](https://github.com/steemit/steem/issues/1268).
This should be included in Token Generation Event / Initial Token Offering section, no?

- `STEEMIT_BLOCKCHAIN_PRECISION` : Configurable
- `STEEMIT_BLOCKCHAIN_PRECISION_DIGITS` : Configurable

## Reward curves

TODO: Write this section

## Target votes per day

TODO: Write this section

## Regeneration time

TODO: Write this section

## Dynamic Rewards Parameters

SMTs have several parameters adjustable at the launch of the token, such as inflation rate, token generation events and founder's issuance, that cannot be changed once the token is launched, however, SMTs also have dynamic parameters that allow the token launcher to adjust certain properties of the token refine the incentivized behaviors of the token's users. Some of the parameters will increase the flow of the rewards pool towards certain user behaviors while reducing the flow towards other less desired behaviors.

- `STEEMIT_CASHOUT_WINDOW_SECONDS` : Dynamic  TODO CASH OUT the name in the chain already? (seems to be a bad name)  WHY IS STEEMIT listed here and not STEEM????
- `STEEMIT_VOTE_REGENERATION_SECONDS` : Dynamic
- `STEEMIT_REVERSE_AUCTION_WINDOW_SECONDS` : Dynamic
- `vote_power_reserve_rate` : Dynamic
- ADD REWARDS CURVE PARAMETERS

### Parameter Constraints

Several dynamic parameters must be constrained to prevent abuse scenarios that could harm token users.

- `0 < STEEMIT_VOTE_REGENERATION_SECONDS < STEEMIT_VESTING_WITHDRAW_INTERVAL_SECONDS`
- `0 <= STEEMIT_REVERSE_AUCTION_WINDOW_SECONDS + STEEMIT_UPVOTE_LOCKOUT < STEEMIT_CASHOUT_WINDOW_SECONDS < STEEMIT_VESTING_WITHDRAW_INTERVAL_SECONDS`
- `0 < SMT_REWARD_CURVE`

## Hardcoded Token Parameters

Hardcoded parameters are aspects of tokens that interact with users in manners that have been found to increase security and safety of the assets as managed by the end user.  Though these hard coded parameters could change for all SMTs in the case of a STEEM-wide upgrade, it is proposed that SMTs leverage these parameters in the same manner as the STEEM asset for the benefit of continuity and common user knowledge.

CAN WE CHANGE STEEMIT TO STEEM IN THE CHAIN?
- `STEEMIT_UPVOTE_LOCKOUT_HF17` : Hardcoded -- This value locks out upvotes from posts at a certain time prior to "CASH OUT" to prevent downvote abuse immediately prior to "CASH OUT."
- `STEEMIT_VESTING_WITHDRAW_INTERVALS` : Hardcoded
- `STEEMIT_VESTING_WITHDRAW_INTERVAL_SECONDS` : Hardcoded
- `STEEMIT_MAX_WITHDRAW_ROUTES` : Hardcoded
- `STEEMIT_SAVINGS_WITHDRAW_TIME` : Hardcoded
- `STEEMIT_SAVINGS_WITHDRAW_REQUEST_LIMIT` : Hardcoded
- `STEEMIT_MAX_VOTE_CHANGES` : Hardcoded
- `STEEMIT_MIN_VOTE_INTERVAL_SEC` : Hardcoded
- `STEEMIT_MIN_ROOT_COMMENT_INTERVAL` : Hardcoded
- `STEEMIT_MIN_REPLY_INTERVAL` : Hardcoded
- `STEEMIT_MAX_COMMENT_DEPTH` : Hardcoded
- `STEEMIT_SOFT_MAX_COMMENT_DEPTH` : Hardcoded
- `STEEMIT_MIN_PERMLINK_LENGTH` : Hardcoded
- `STEEMIT_MAX_PERMLINK_LENGTH` : Hardcoded
- `STEEMIT_MAX_SHARE_SUPPLY` : Hardcoded

## SMT Parameters Commentary

# Decentralized Exchange
One of the valuable features of SMTs is their immediate access to functioning, unmanned markets against the liquid asset, STEEM.

## Decentralized Order Matching
The Decentralized Exchange (DEX) structures of Steem allow assets to automatically be matched for best possible price when bids and asks overlap, unlike other DEXs which require a man in the middle to match orders.  This is important for security of Steem-based assets and for the replicability and safety of DEX interfaces.

## Diverse Asset Types
There are several assets that SMT users and creators will have access to by way of the Steem DEX: STEEM; SBD; SMTs; Simple Derivatives (IOUs).  These neighboring assets can increase the visibility and network effect of all created SMTs.

STEEM is the gateway token for assets issued on Steem, staying relevant by acting as the bandwidth usage measuring stick across Steem's meta-assets.  STEEM is also the common denominator asset, acting as a trading pair for all of Steem's meta-assets.

SBD (Steem Blockchain Dollars) are an experimental asset on Steem that relate to the US Dollar originating back to Steem's launch in 2016. It is unclear if SBD will bring value to holders of USD as they will compete, possibly poorly, with IOU USDs, however, SBDs will bring value to speculators.

SMTs as described in this proposal are an important part of growing the token ecosystem and bringing crypto assets to the mainstream.  SMTs will trade against STEEM across the DEX.

Simple Derivatives (IOUs) will be possible via SMT issuance.  For instance, if an SMT is issued without inflation or rewards pool properties, then the issuer can reliably back the token with another real world asset such as bitcoin or USD.  In this instance, the issuer could create business as a gateway by trading their IOU for btc or USD.  Users would buy the IOU to gain access to the Steem DEX. This market would add diversity and value flow to the Steem ecosystem while adding to the DEX's network effect.

## ZERO Trading Fees
The Steem DEX is the first DEX to exist without trading fees, to the benefit of SMT creators and traders alike.  This is made possible by Bandwidth Rate Limiting, a concept first introduced in the original Steem White Paper.

# Ecosystem Support

# Conclusion
