CONFIDENTIAL AND PRIVILEGED; DO NOT SHARE
Proposal by Steemit Inc
Copyright (c) Steemit, Inc. 2017
Status: DRAFT

# Smart Media Tokens 

Steem Proposal: A Token Issuance Protocol for Fundraising and Autonomous Growth

- [Introduction](#introduction)
- [Owner's manual](#owners-manual)
  - [Establish a Name Space](#establish-a-name-space)
    - [Token consensus](#token-consensus)
  - [Token Generation and Initialized Parameters](#token-generation-and-initialized-parameters)
    - [Creation fee](#creation-fee)
    - [SMT setup](#smt-setup)
    - [Token units](#token-units)
    - [Unit ratios](#unit-ratios)
    - [Cap and min](#cap-and-min)
    - [Hidden caps](#hidden-caps)
    - [Generation policy data structure](#generation-policy-data-structure)
    - [Examples and rationale](#examples-and-rationale)
      - [Example TGE](#example-tge)
      - [Why unit ratios?](#why-unit-ratios)
      - [UI treatment of unit ratios](#ui-treatment-of-unit-ratios)
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
    - [Inflation Parameters](#inflation-parameters)
      - [Possible inflation target](#possible-inflation-target)
      - [Event sequences](#event-sequences)
      - [Adding relative inflation](#adding-relative-inflation)
      - [Adding time modulation](#adding-time-modulation)
      - [Inflation operations](#inflation-operations)
      - [Inflation FAQ](#inflation-faq)
    - [Token Precision Parameters](#token-precision-parameters)
  - [Vesting rewards](#vesting-rewards)
  - [Content rewards](#content-rewards)
  - [Curve definitions](#curve-definitions)
  - [Target votes per day](#target-votes-per-day)
  - [Dynamic Rewards Parameters](#dynamic-rewards-parameters)
    - [Parameter Constraints](#parameter-constraints)
  - [Hardcoded Token Parameters](#hardcoded-token-parameters)
  - [SMT Parameters Commentary](#smt-parameters-commentary)
- [Decentralized Exchange](#decentralized-exchange)
  - [Decentralized Order Matching](#decentralized-order-matching)
  - [Diverse Asset Types](#diverse-asset-types)
  - [ZERO Trading Fees](#zero-trading-fees)
- [Ecosystem Support](#ecosystem-support)
  - [How to integrate tokens](#how-to-integrate-tokens)
  - [Existing publisher](#existing-publisher)
  - [New application](#new-application)
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

   time_point_sec          generation_end_time;
   time_point_sec          launch_time;

   extensions_type         extensions;
};
```

The operation must be signed by the `control_account` key.  The name
of the control account becomes the name of the token.  The
`decimal_places` field is used by UI's to display units as a number
of decimals.

### Token units

Initial token generation is driven by a contributions of *STEEM
units* from contributors.  To simplify rounding concerns, a
contribution must be an integer number of STEEM units.  The TGE
creator sets the size of a STEEM unit, it can be large or small.
It is better to keep the unit small (for example, 1 STEEM or
0.1 STEEM), as this allows the TGE to be accessible to the
maximum possible audience.

A STEEM unit also specifies a *routing policy* which determines
where the STEEM goes when the token launches.  (STEEM for tokens
which do not launch may be refunded on demand.)  The routing
policy may split the STEEM in the unit among multiple parties.

When the TGE occurs, the tokens are generated in *token units*.
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

The maximum number of token units that can be created in the TGE
is limited to `max_token_units_generated`, a parameter which is set by
the TGE creator.  (More tokens can be created after the
token has launched, but this later creation is called *inflation*
and is not considered to be part of the TGE.)

The unit ratio is set to the largest integer that would
not result in exceeding `max_token_units_generated` for the number
of STEEM units actually contributed.

### Cap and min

TGE's may specify a minimum number of STEEM units `min_steem_units`.
If the TGE does not reach `min_steem_units` before `generation_end_time`,
then it does not occur and contributors become eligible for refunds.

Likewise, TGE's may specify two maximum numbers of STEEM units:
A *hard cap* and a *soft cap*.  Units in excess of the soft cap
have different routing for their STEEM and tokens.  STEEM units in
excess of the hard cap are rejected and do not generate any SMT's.

The effects of the soft cap are divided equally among all contributors.
I.e. if a TGE has a soft cap of 8 million STEEM, and 10 contributors
each contribute 1 million STEEM, then 0.2 million of
*each user's* STEEM is routed via the soft cap's policy.

The effects of the hard cap fall solely on the last contributors.
I.e. if a TGE has a hard cap of 8 million STEEM, and 10 contributors each
contribute 1 million STEEM, then the first 8 users fully participate
in the TGE, and the last 2 users are refunded 1 million STEEM.

### Hidden caps

The min and hard cap are *hidden* in the generation policy.  This means
that these numbers are fixed at setup time, but the TGE creator has the
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
Therefore, a TGE with a non-hidden minimum or cap may be implemented by
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

   uint16_t            soft_cap_percent;

   uint32_t            min_unit_ratio;
   uint32_t            max_unit_ratio;

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

#### Example TGE

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
Therefore the unit ratio of this TGE is 1000.  This unit ratio is placed in
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

### Launch

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

### Examples

#### Full JSON example

Suppose BETA is defined with the following definitions:

TODO:  Fix/update this JSON

  


```
[
 ["SMT_setup_operation",
  {
   "control_account"           : "beta",
   "decimal_places"            : 4,
   "max_supply"                : STEEMIT_MAX_SHARE_SUPPLY,
   "initial_generation_policy" : [0,
	{
	 "pre_soft_cap_unit"          : {
	  "steem_unit":[],
	  "token_unit":[]
	 },
	 "post_soft_cap_unit"         : {
	  "steem_unit":[],
	  "token_unit":[]
	 },
	 "min_steem_units_commitment" : {
	  "lower_bound":0,
	  "upper_bound":0,
	  "hash":"abcd123"
	 },
	 "hard_cap_steem_units_commitment" : {
	  "lower_bound" : 0,
	  "upper_bound" : 0,
	  "hash"        : "abcd123"
	 },
	 "soft_cap_percent":0, 
	 "min_unit_ratio":0, 
	 "max_unit_ratio":0, 
	 "extensions":[] 
	}
   ],
   "generation_end_time"       : "2017-06-01T00:00:00",
   "launch_time"               : "2017-06-01T00:00:00",
   "extensions"                : []
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

#### Single-segment with min and cap

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

#### Fixed-float no-reserve

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

#### Vesting contributions

It is possible to send part or all of contributions
to a vesting balance, instead of permitting immediate
liquidity.  This example puts 95% in vesting.

```
"token_unit"           : [["$from.vesting", 95], ["$from", 5]]
```

#### Burning contributed STEEM

In this ITO, the STEEM is permanently destroyed rather than going into the wallet of any person.
This mimics the structure of the Counterparty ITO.

```
{
 "steem_unit" : [["null", 1]],
 "token_unit" : [["$from", 1]]
}
```

#### Vesting as cost

In this ITO, you don't send STEEM to the issuer in exchange for tokens.  Instead, you vest STEEM (to yourself),
and tokens are issued to you equal to the STEEM you vested.

```
{
 "steem_unit" : [["$from.vesting", 1]],
 "token_unit" : [["$from", 1]]
}
```

#### Non-STEEM & Hybrid ITO's

ITO's using non-STEEM contributions -- for example, SBD, BTC, ETH, etc. --
cannot be done fully automatically on-chain.   However, such ITO's can be
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

TODO:  Add more text.  Can we re-use data type for `inflation_target`?

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

## Vesting rewards

TODO:  Do we want to rename vesting rewards to powerup rewards?

Token inflation may be directed to vesting rewards.  These rewards are effectively
split among all users with vesting balances proportional to the number of tokens
they have vested.  As the number of tokens devoted to these rewards is independent
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

TODO:  File a ticket to rename `quadratic_curation` to `bounded` in the code

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
For STEEM itself, curation was originally the quadratic `ICR=`, as of (TODO: Hardfork number) it is the linear `ICR=`.

TODO:  Operator to create fund
TODO:  Do we want to allow these parameters to be dynamic?
TODO:  Possibly decreasing-slope reward curve?
TODO:  Possibly `ICR-` curve for quadratic?

## Target votes per day

Each account has a `voting_power`, which is essentially a "mana bar" that fills from 0% to 100% over time at a constant rate.
That rate is determined by two parameters:

- (a) The time it takes to regenerate the bar to 100%, `vote_regeneration_period_seconds`
- (b) The `voting_power` used by a maximum-strength vote

The `vote_regeneration_period_seconds` is specified directly.  For (b), instead of
specifying the voting power of a maximum-strength vote directly, instead you specify
`votes_per_regeneration_period`.  Then the maximum-strength vote is set such that a
user casting that many max-strength votes will exactly cancel the regeneration.

TODO:  File ticket to change from target votes per day to target votes per period
TODO:  File ticket to refactor out voting computations
TODO:  Make voting power upper bound constant, delegate voting power decision to UI
TODO:  Create operation.

## Dynamic Rewards Parameters

SMTs have several parameters adjustable at the launch of the token, such as inflation rate, token generation events and founder's issuance, that cannot be changed once the token is launched, however, SMTs also have dynamic parameters that allow the token launcher to adjust certain properties of the token refine the incentivized behaviors of the token's users. Some of the parameters will increase the flow of the rewards pool towards certain user behaviors while reducing the flow towards other less desired behaviors.

- `STEEMIT_CASHOUT_WINDOW_SECONDS` : Dynamic  TODO CASH OUT the name in the chain already? (seems to be a bad name)  WHY IS STEEMIT listed here and not STEEM????
- `STEEMIT_VOTE_REGENERATION_SECONDS` : Dynamic
- `STEEMIT_REVERSE_AUCTION_WINDOW_SECONDS` : Dynamic
- `vote_power_reserve_rate` : Dynamic
- `STEEMIT_CONTENT_REWARD_PERCENT` : Dynamic
- `STEEMIT_VESTING_FUND_PERCENT` : Dynamic

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

## How to integrate tokens

## Existing publisher

## New application

# Conclusion
