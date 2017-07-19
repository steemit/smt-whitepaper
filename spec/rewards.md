
# Rewards allocation

## Reward pool naming

When a token descriptor is created, a reward pool object of the same name as the token
will be created.

## Community consensus changes

A `comment_options_extension` called `extra_rewards_pool` is added, which indicates the
name of an additional reward pool for which a post is eligible.

No consensus level validation is performed on `extra_rewards_pool`.  As a consequence,
any post may mark itself as eligible for any rewards pool.  However, UI's may impose
their own non-consensus validation rules on `extra_rewards_pool`, and hide posts
that violate these non-consensus validation rules.

For example, in a Hive community, there may be a validation rule that the
`extra_rewards_pool` specified in each post in that Hive community must match the
reward pool of that community.  This is a non-consensus validation rule, since the
entire concept of a post existing in a Hive community is a non-consensus concept.
Since it is a non-consensus validation rule, no consensus logic can enforce it.
However, UI's that are aware of Hive communities may refuse to index or display
posts that violate this validation rule.

## Reward splitting

The STEEM rewards for post upvoters is determined by the STEEM algorithm based on vesting
STEEM.  The CBT rewards for post upvoters is determined by the CBT reward pool's algorithm
and the upvoter's vesting balance of that CBT.

If an upvoter has a VB of STEEM and the CBT, then they get both STEEM and CBT rewards.

## Ranking of posts

The ranking of posts provided by `steemd` will continue to be solely based on STEEM.  UI's
are free to rank posts by some other method.  For example:

- Rank posts by CBT rshares
- Rank posts by some linear combination of STEEM rshares and CBT rshares
- Rank posts by valuing STEEM rshares and CBT rshares using current exchange rate of STEEM and CBT

## Reward pool algorithms

Each reward pool specifies the following:

- Reward curve, specifying how much a post gets as a function of upvotes
- Curation curve, specifying how much advantage earlier curators have over later curators
- Content constant, specifies scaling factor for some reward / curation curves
- Time constant, specifies how much the reward fund buffers changes in user behavior
- Post/comment/vote split, specifying how much goes to top-level posts, how much goes to comments, how much goes to upvoters

## Available reward curve

- `quadratic`          : `f(r) = (r+s)^2 - s^2`
- `quadratic_curation` : `f(r) = r / (r+2s)`
- `linear`             : `f(r) = r`
- `square_root`        : `f(r) = sqrt(r)`

Restrictions:

- `quadratic + quadratic_curation`
- `linear + linear`
- `linear + square_root`

## Changing reward curve

A change to the reward curve and parameters can be initiated at any time by the asset creator.
The change is deferred for a window equal to the previous time constant, and replaces any
existing currently pending change.  The window is used to initialize recent claims.  After the
window expires, the new settings apply to future rewards.  Note the asset creator cannot use
these settings to change the amount of inflation used to fund the reward pool, nor can the creator
send inflated tokens to any specific author or content.

