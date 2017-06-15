
# Token issue segments

AGS style distribution divided into segments.

```
struct token_issue_segment
{
   timestamp           start_time;
   timestamp           end_time;
   asset               max_contribution;
   asset               max_issue;
   price               min_price;
};
```

1. Reject STEEM contributions that would cause `max_contribution` to be exceeded.
2. Attempt to issue tokens to all contributions at `min_price`.
3. If (2) would cause `max_issue` to be exceeded, issue `max_issue` tokens to all contributors proportionally to their contribution.

FAQ:

- Q: How do I allow unlimited contributions?  A: Set `max_contribution` to a very large number.
- Q: How do I issue a variable quantity of tokens at a fixed price?  A: Set `max_issue` to a very large number and `min_price` to the desired price.
- Q: How do I issue a fixed quantity of tokens proportionally to contributors' contributions?  A: Set `min_price` to a very small number and set `max_issue` to the desired quantity of tokens.

# Targets

Specify who gets the issued tokens.

```
struct token_issue_target_spec
{
   flat_map< account_name_type, uint16_t >        steem_targets;
   flat_map< account_name_type, uint16_t >        token_targets;
};
```

# Target accounts

The `token_targets` account has a special account name, `$from`, which should be illegal
to be created, and will represent the contributor.

Also supported is `$from.vesting` which represents the vesting balance of the `$from`
account.

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

### Repeated fixed-price sales at different prices

Tokens sold in the first days are sold 1-1, later on tokens are sold at a slightly higher price.
This may be done by repeating the segment.  This can mimic the structure of the Ethereum ICO.

### Tokens for ICO owner

This ICO is the same as one-token-per-STEEM, but in addition 30% of the tokens created goes to `catman`.

```
"token_targets" : [{"$from" : 7, "catman" : 3}]
```

### Fixed quantity no-reserve auction

In this ICO, we divide 1 million CAT among contributors according to their contribution.

```
{
 "segments" :
 [
  {
   "start_time" : "2017-01-01T00:00:00", "end_time" : "2017-01-04T00:00:00",
   "max_contribution" : "1 billion STEEM", "max_issue" : "1000000 CAT",
   "min_price" : "0.001 STEEM / CAT"
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

### Fixed quantity serial no-reserve auction

Repeating the segment in the previous auction with different dates allows AGS style auction.
Each day has an allotment of coins are divided among contributors according to their contribution.
This mimics the structure of the AngelShares ICO for BitShares.

### Burning contributed STEEM

In this ICO, the STEEM is permanently destroyed rather than going into the wallet of any person.
This mimics the structure of the Counterparty ICO.

```
{
 "steem_targets" : [{"null" : 1}],
 "token_targets" : [{"$from" : 1}]
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

### Locking up shares

Consider Ripple's announcement that it will add on-blockchain restriction to sales of its reserve as
discussed in [this article](https://www.americanbanker.com/news/inside-ripples-plan-to-make-money-move-as-fast-as-information).
TODO: Primary source

To implement something similar for STEEM, we would allow an account to be created with a permanently
smaller maximum vesting withdrawal rate.  The maximum vesting withdrawal rate should not be changeable
after account creation because it is a potential route for a hacker to permanently damage an account
in a way that account recovery cannot fix.

### Vesting as cost

In this issue, you don't send STEEM to the issuer in exchange for tokens.  Instead, you vest STEEM (to yourself),
and tokens are issued to you equal to the STEEM you vested.

```
{
 "steem_targets" : [{"$from.vesting" : 1}],
 "token_targets" : [{"$from" : 1}]
}
```

### Non-STEEM ICO's

ICO's using SBD or other tokens are deliberately not supported.  The implementation would be more
complicated, and STEEM holders are less able to capture value if ICO's don't use STEEM as the base.

### Market maker accounts

Market making is done by performing a "ping" to the MM account.  This inspects the state of the
market and issues orders from the MM account as appropriate.  The pinger is responsible for
paying the bandwidth cost of the ping.

An account which is created as a market maker has `mm_ping_authority` and `mm_reserve_ratios`.
To create a fully decentralized market maker, create an account with no recovery account, set
`mm_ping_authority` to `temp`, and set the account's owner/active/posting authorities to `null`.
Funds in the account will then be inaccessible and it will operate completely autonomously.

TODO:  Specify fee percentage, fee beneficiary

### Whitelist

Some ICO's want to do KYC or some other form of due diligence on customers.  Charles Hoskinson's
Japan coin (TODO:  what is this project called?) falls into this category.

This is going to be complicated to support, let's skip it.

### Multi-stage ICO

Some ICO's want to change the `token_target_issue_spec` or otherwise modify the ICO once a certain
target has been reached.  This allows a Bancor-style ICO where additional funds beyond the cap aren't
rejected, but are instead directed to decentralized market maker.

TODO:  How do we modify the data structures to enable this use case?
