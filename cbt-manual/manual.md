# Smart Media Tokens
## Outline

TODO:  Links from here to section anchors later
TODO:  Can we make anchor names portable across markdown engines?

1. Introduction - (Value Prop) - Proposal for Steem
**2.Owner's Manual
2a. Establish Name Space & Token Creation
2a1. Tokens are consensus with the Steem name space
2a2. There is a fee for launching a token, paid to the blockchain.

**2b. Token Parameters
2b1. Descriptor
2b2. ICO
2b3. Market Maker
2b4. Inflation
2b5. Structures
2b6a. Rewards Curves
2b6b. Target Votes Per Day
2b6c. Regeneration times
2b6d. ... All other Structures/Parameters**

3. Ecosystem Apps Supporting SMTs
4. Conclusion

# Introduction

TODO:  Talk about value proposition, proposal for STEEM

# Owner's manual

This manual will explain the nuts and bolts of how SMT's work.
The intended audience is technical users who want to create their
own SMT.

## Reserving a name

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

### Creation fee

TODO:  Explain and justify the blockchain's fee to create an asset

## Token parameters

### Descriptor

Each SMT has an associated descriptor object which has
*permanent configuration data*.  This data cannot be changed after launch!
The descriptor is set by the `SMT_setup_operation`:

```
struct SMT_setup_operation
{
   account_name_type       control_account;
   uint8_t                 decimal_places = 0;
   int64_t                 max_supply = STEEMIT_MAX_SHARE_SUPPLY;

   SMT_distribution        initial_distribution_policy;

   extensions_type         extensions;
};
```

SMT token creation exchange takes place in a series of *units*.

### ICO

TODO:  Is ICO a term we want to use?

ALPHA wants to create a crowdsale (TODO: is this the term we want to use?)
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

The answer is that it is possible to write crowdsale definitions for which
price is ill-defined.  For example:

- `"$from"` does not occur in `token_unit`
- `"$from"` occurs in both `token_unit` and `steem_unit`
- A combination of `"$from"` and `"$from.vesting"` occurs
- Future expansion allows new special accounts

These definitions are still supported by unit ratio.

#### UI treatment of unit ratios

As a consequence of the above, the concept of "crowdsale price" is purely
a UI-level concept.  UI's which provide a crowdsale price should do the following:

- Document the precise definition of "price" provided by the UI
- Be well-behaved for pathological input like above
- Have a button for switching between a unit ratio display and price display

#### Defining SMT units

The operation used to define units is:

```
struct SMT_define_unit_operation
{
   account_name_type                              control_account;
   uint32_t                                       unit_num = 0;
   flat_map< account_name_type, uint16_t >        steem_unit;
   flat_map< account_name_type, uint16_t >        token_unit;

   extensions_type                                extensions;
};
```

##### Special account names

The `token_unit` member allows a special account name, `$from`, which should be illegal to be created, and will represent the contributor.

Also supported is `$from.vesting` which represents the vesting balance of the `$from` account.

#### Defining SMT issue segments

A *segment* is a portion of a SMT.  During the contribution phase of a SMT,
exactly one segment is active at any point in time.  The transition from
one segment to the next is triggered either by passing a specific point in
time, or by exceeding a predefined cap.

SMT issue segments are defined with the following operation:

```
struct SMT_define_segment_operation
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

In this ICO, the STEEM is permanently destroyed rather than going into the wallet of any person.
This mimics the structure of the Counterparty ICO.

```
{
 "steem_unit" : [["null", 1]],
 "token_unit" : [["$from", 1]]
}
```

##### Vesting as cost

In this ICO, you don't send STEEM to the issuer in exchange for tokens.  Instead, you vest STEEM (to yourself),
and tokens are issued to you equal to the STEEM you vested.

```
{
 "steem_targets" : [["$from.vesting", 1]],
 "token_targets" : [["$from", 1]]
}
```

# Example ICO's

### One-token-per-STEEM

In this 3-day ICO, one STEEM will be one CAT.  ICO proceeds go to `catman` account, the CAT promoter.

```
{
 "segments" :
 [
  {
   "start_time" : "2017-01-01T00:00:00", "end_time" : "2017-01-04T00:00:00",
   "max_contribution" : "1 billion STEEM", "max_issue" : "1 billion CAT",
   "min_price" : "1.0 STEEM / CAT"
  }
 ],
 "target_spec" :
 [
  {
   "steem_targets" : [{"catman" : 1}],
   "token_targets" : [{"$from" : 1}]
  }
 ]
}
```

### Locking up tokens

In this ICO, 95% of the tokens go to vesting balance object (VBO).

```
{
 "steem_targets" : [{"catman" : 1}],
 "token_targets" : [{"$from.vesting" : 19, "$from" : 1}]
}
```

### Non-STEEM ICO's

ICO's using SBD or BTC or ETH and other tokens are not supported by complete on chain ICOs, however, they can be managed by manually transferring founder's distributions to buyers' Steem accounts in proportion to their donation in the non-STEEM assets.

### Market maker accounts

Market making is done by performing a "ping" to the MM account.  This inspects the state of the
market and issues orders from the MM account as appropriate.  The pinger is responsible for
paying the bandwidth cost of the ping.

An account which is created as a market maker has `mm_ping_authority` and `mm_reserve_ratios`.
To create a fully decentralized market maker, create an account with no recovery account, set
`mm_ping_authority` to `temp`, and set the account's owner/active/posting authorities to `null`.
Funds in the account will then be inaccessible and it will operate completely autonomously.

TODO:  Specify fee percentage, fee beneficiary

### Multi-stage ICO

Some ICO's want to change the `token_target_issue_spec` or otherwise modify the ICO once a certain
target has been reached.  This allows a Bancor-style ICO where additional funds beyond the cap aren't
rejected, but are instead directed to decentralized market maker.

TODO:  How do we modify the data structures to enable this use case?

TODO:  Rename this because "multi-stage ICO" already means something else in the industry

### Future feature list

- Idea:  Return excess funds above cap to investors
- Support for hidden cap
- BitShares lessons learned from flags
- Don't have permission bits, mutations of flags need to be scheduled in advance
- Interesting type of asset:  Can participate in market, but not transferrable
- Figure out how deferred issuance works
- UI / scripts to generate segments

The triumvirate

- Descriptor (name, decimals, boring stuff)
- Issuance
- Inflation
- 
- 
# Inflation

Token creation is called *inflation*.

Inflation is the means by which the SMT rewards contributors for
the value they provide.

Inflation events use the following data structure:

```
// Event:  Support issuing tokens to target at time
struct token_inflation_event
{
   timestamp           schedule_time;
   asset               new_SMT;
   inflation_target    target;
};
```

This event prints `new_SMT` amount of the SMT token and sends it to the
given `target` account.

# Possible inflation target

The target is the entity to which the inflation is directed.  The target
may be a normal Steem account controlled by an individual founder, or a
multisig of several founders.

In addition, several special targets are possible representing trustless
functions provided by the blockchain itself:

- Rewards.  A special destination representing the token's posting / voting rewards.
- Vesting.  A special destination representing the tokens backing vested tokens.
- Market maker.  A special destination representing a CRR market maker.

# Event sequences

A single inflation event is insufficient.

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
   asset               new_SMT;
   inflation_target    target;

   int32_t             interval_seconds;
   uint32_t            interval_count;
};
```

The data structure represents a token inflation event
that repeats every `interval_seconds` seconds, for
`interval_count` times.  The maximum integer value
`0xFFFFFFFF` is a special sentinel value that represents
an event sequence that repeats forever.

# Adding relative inflation

Often, inflation schedules are expressed using percentage
of supply, rather than in absolute terms:

```
// Event seq v2:  v1 + allow relative amount of tokens
struct token_inflation_event_seq_v2
{
   timestamp           schedule_time;
   inflation_target    target;

   int32_t             interval_seconds;
   uint32_t            interval_count;

   asset               abs_amount;
   uint32_t            rel_amount_numerator;
};
```

Then we compute `new_SMT` as follows from the supply:

```
rel_amount = (SMT_supply * rel_amount_numerator) / SMT_REL_AMOUNT_DENOMINATOR;
new_SMT = max( abs_amount, rel_amount );
```

If we set `SMT_REL_AMOUNT_DENOMINATOR` to a power of two, the division
can be optimized to a bit-shift operation.  To gain more dynamic range
from the bits, we can let the shift be variable:

```
// Event seq v3:  v2 + specify shift in struct
struct token_inflation_event_seq_v3
{
   timestamp           schedule_time;
   inflation_target    target;

   int32_t             interval_seconds;
   uint32_t            interval_count;

   asset               abs_amount;
   uint32_t            rel_amount_numerator;
   uint8_t             rel_amount_denom_bits;
};
```

Then the computation becomes:

```
rel_amount = (SMT_supply * rel_amount_numerator) >> rel_amount_denom_bits;
new_SMT = max( abs_amount, rel_amount );
```

Of course, an implementation of these computations must carefully handle
potential overflow in the intermediate value `SMT_supply * rel_amount_numerator`!

# Adding time modulation

Time modulation allows implementing an inflation rate which changes continuously
over time according to a piecewise linear function.  This can be achieved by simply
specifying the left/right endpoints of a time interval, and specifying absolute amounts
at both endpoints:

```
// Event seq v4:  v3 + modulation over time
struct token_inflation_event_seq_v4
{
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
   rel_amount_numeratr = lep_rel_amount_numerator * (1-t) + rep_rel_amount_numerator * t;
}
```

# FAQ

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

## Parameter constraints

- `0 < STEEMIT_VOTE_REGENERATION_SECONDS < STEEMIT_VESTING_WITHDRAW_INTERVAL_SECONDS`
- `0 <= STEEMIT_REVERSE_AUCTION_WINDOW_SECONDS + STEEMIT_UPVOTE_LOCKOUT < STEEMIT_CASHOUT_WINDOW_SECONDS < STEEMIT_VESTING_WITHDRAW_INTERVAL_SECONDS`

## Dynamic parameters

- `STEEMIT_CASHOUT_WINDOW_SECONDS` : Dynamic
- `STEEMIT_VOTE_REGENERATION_SECONDS` : Dynamic
- `STEEMIT_REVERSE_AUCTION_WINDOW_SECONDS` : Dynamic
- `vote_power_reserve_rate` : Dynamic

## Configurable parameters

- `STEEMIT_BLOCKCHAIN_PRECISION` : Configurable
- `STEEMIT_BLOCKCHAIN_PRECISION_DIGITS` : Configurable

## Hardcoded parameters

- `STEEMIT_UPVOTE_LOCKOUT_HF17` : Hardcoded
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

