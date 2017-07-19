
# Introduction

This manual will explain the nuts and bolts of how CBT's work.
The intended audience is technical users who want to create their
own CBT.

# Status

This document describes functionality which has not yet been
implemented.  Therefore, many/most/all of the practical interfaces
and examples do not actually work yet.

# Testnet

It is *highly recommended* that a private or public Steem testnet
is used to test all operations and transactions related to custom
asset issuance, before issuing them on the main blockchain.

(TODO:  Provide a link to information on public and private testnets,
when such information is written.)

# Reserving a name

After you've decided on a name for your CBT, you are ready to create
the CBT's *control account*.  This control account will be able to
design the CBT's policies, launch the CBT, and modify certain CBT
parameters after launch.

The CBT's name will be the same as the name of its control account.

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

# Descriptor

Each CBT has an associated descriptor object which has
*permanent configuration data*.  This data cannot be changed after launch!
The descriptor is set by the `cbt_setup_operation`:

```
struct cbt_setup_operation
{
   account_name_type       control_account;
   uint8_t                 decimal_places = 0;
   int64_t                 max_supply = STEEMIT_MAX_SHARE_SUPPLY;

   cbt_distribution        initial_distribution_policy;

   extensions_type         extensions;
};
```

# CBT token creation mechanics

CBT token creation exchange takes place in a series of *units*.

## Example

ALPHA wants to create a crowdsale (TODO: is this the term we want to use?)
where 7% of contributed STEEM
goes to Founder Account A, 23% of contributed STEEM goes to Founder
Account B, and 70% of contributed STEEM goes to Founder Account C.

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

## Why unit ratios?

Why does the blockchain use unit ratios, rather than simply specifying
prices?

The answer is that it is possible to write crowdsale definitions for which
price is ill-defined.  For example:

- `"$from"` does not occur in `token_unit`
- `"$from"` occurs in both `token_unit` and `steem_unit`
- A combination of `"$from"` and `"$from.vesting"` occurs
- Future expansion allows new special accounts

These definitions are still supported by unit ratio.

## UI treatment of unit ratios

As a consequence of the above, the concept of "crowdsale price" is purely
a UI-level concept.  UI's which provide a crowdsale price should do the following:

- Document the precise definition of "price" provided by the UI
- Be well-behaved for pathological input like above
- Have a button for switching between a unit ratio display and price display

## Defining CBT units

The operation used to define units is:

```
struct cbt_define_unit_operation
{
   account_name_type                              control_account;
   uint32_t                                       unit_num = 0;
   flat_map< account_name_type, uint16_t >        steem_unit;
   flat_map< account_name_type, uint16_t >        token_unit;

   extensions_type                                extensions;
};
```

## Defining CBT issue segments

A *segment* is a portion of a CBT.  During the contribution phase of a CBT,
exactly one segment is active at any point in time.  The transition from
one segment to the next is triggered either by passing a specific point in
time, or by exceeding a predefined cap.

CBT issue segments are defined with the following operation:

```
struct cbt_define_segment_operation
{
   account_name_type   control_account;
   time_point_sec      end_time;

   uint32_t            unit_num;

   uint32_t            min_steem_units;
   uint32_t            max_steem_units;

   uint32_t            begin_unit_ratio;
   uint32_t            end_unit_ratio;

   extensions_type     extensions;
};
```

The ratios must be defined with `begin_unit_ratio >= end_unit_ratio > 0`.

## Example

Suppose BETA is defined with the following definitions:

```
[
 ["cbt_setup_operation",
  {
   "control_account"      : "beta",
   "decimal_places"       : 4,
   "max_supply"           : STEEMIT_MAX_SHARE_SUPPLY,
   "launch_time"          : "2017-06-01T00:00:00"
  },
 ],
 ["cbt_define_unit_operation",
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
 ["cbt_define_segment_operation",
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

## Single-segment with min and cap

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

## Fixed-float no-reserve

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

## Vesting contributions

It is possible to send part or all of contributions
to a vesting balance, instead of permitting immediate
liquidity.  This example puts 95% in vesting.

```
"token_unit"           : [["$from.vesting", 95], ["$from", 5]]
```
