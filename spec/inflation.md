
# Inflation

Token creation is called *inflation*.

Inflation is the means by which the CBT rewards contributors for
the value they provide.

Inflation events use the following data structure:

```
// Event:  Support issuing tokens to target at time
struct token_inflation_event
{
   timestamp           schedule_time;
   asset               new_cbt;
   inflation_target    target;
};
```

This event prints `new_cbt` amount of the CBT token and sends it to the
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
production for CBT's.  In fact, CBT's have no block rewards,
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
   asset               new_cbt;
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

Then we compute `new_cbt` as follows from the supply:

```
rel_amount = (cbt_supply * rel_amount_numerator) / CBT_REL_AMOUNT_DENOMINATOR;
new_cbt = max( abs_amount, rel_amount );
```

If we set `CBT_REL_AMOUNT_DENOMINATOR` to a power of two, the division
can be optimized to a bit-shift operation.  To gain more dynamic range
from the bits, we can let the shift be variable:

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
   uint8_t             rel_amount_denom_bits;
};
```

Then the computation becomes:

```
rel_amount = (cbt_supply * rel_amount_numerator) >> rel_amount_denom_bits;
new_cbt = max( abs_amount, rel_amount );
```

Of course, an implementation of these computations must carefully handle
potential overflow in the intermediate value `cbt_supply * rel_amount_numerator`!

# Adding time modulation

Time modulation allows implementing an inflation rate which changes continuously
over time according to a piecewise linear function.  This can be achieved by simply
specifying the left/right endpoints of a time interval, and specifying absolute amounts
at both endpoints:

```
// Event seq v3:  v2 + modulation over time
struct token_inflation_event_seq_v3
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

TODO:  Make some pretty graphs
TODO:  Examples:  Steem old inflation scheme, Steem new inflation scheme, Bitcoin, send % to founders, send % to founders after time
