
Chapters

Business whitepaper

- 

Tech whitepaper

- Why C#
- Parallelism via two-way sidechaining
- JSON type schemas



# Why C sharp:  A radical departure from Bitcoin

(c) 2017 Steemit, Inc.  All rights reserved.

CONFIDENTIAL:  STEEMIT, INC. INTERNAL USE ONLY

## Introduction

After some evaluation, we have decided to write the DOT prototype in C#, and suggest C# as a language for the full implementation.
This paper we will explain our rationale.

## Problems with C++

It has become clear that C++ as a whole, and specifically the brand of C++ we use to develop blockchains (C++11 with FC), is problematic.
The C++ `steemd` blockchain implementation, the cornerstone of Steemit's main product, is written in C++.

C++ is a very old language, having first appeared in 1983, and being based on the C language, approximately a decade older.  The characteristics
and limitations of the languages are a product of that era.  Despite various modernization efforts, some of the technical aspects are showing their age.
Specific problems with the language itself include:

- Raw memory access, no array bounds checks makes it easier to create programs with certain hard-to-diagnose errors
- No type reflection / introspection makes tooling to manipulate types hard to implement
- No built-in VM layer means VM environments written in C++ are usually interpreted (slow) or produce native code (hard, nonportable, unsafe)
- C++ using text-based inclusion to import declarations is inefficient
- Extensive template usage makes compiling memory-intensive and slow (we pay for an expensive machine for CI, but compiling on it still takes a long time)
- C++ forward declaration means order in which code is written / files are included matters

![How long does compiling C++ take?](ci-lunch-break.png)

As of this writing (May 3, 2017), the previous day two backend developers collectively spent
approximately six man-hours devoted to diagnosing a compiler error in newly written
code.  As with many issues related to C++ templates, the error messages produced by
the code were extremely verbose and unhelpful.

It turns out that changing the order in which files are included can break or fix certain
errors.  This is an issue specifically due to C++ historical baggage.

![Simple example of the problem that cost us 6 man-hours, from cppreference.com](order-matters.png)

This is simply the most recent example of the many, many technical issues due to C++ that
steepen the learning curve for new junior developers and consume the time of experienced
senior developers.

## Wisdom of the crowd

Here's a snapshot of StackOverflow's survey of developers:

![Do people use C#?](do-people-use-csharp.png)

When large parts of an industry choose option 1 over option 2, we should maybe ask ourselves
if there is an economic reason why.  The top two choices on this chart (JavaScript and SQL)
are near-monopolies in their respective domains (JavaScript for web, SQL for "traditional"
databases).

The third language, C#, appears here because of *developer productivity*.  C# is good for
developers because:

- Modern statically typed language
- Developed and supported by a major company (Microsoft)
- "Industrial strength" runtime including JIT compiler, reasonable performance
- Thriving ecosystem with lots of libraries and tooling
- Advanced IDE's and development environments

## Why C++ doesn't matter any more

Here are the main reasons for using C++:

- (a) The C++ language was a favorite of our former CTO.
- (b) Other blockchains are written in C++.
- (c) C++ has superior performance.

And here's why they're not relevant to DOT:

- (a) Our former CTO no longer works here; his preferences should have no bearing on this project.
- (b) We make our reputation by challenging conventional wisdom in blockchain and the choices of Bitcoin and other early projects.

For reason (c), there's a longer explanation.  An argument can be made that traditional
blockchains, being limited to a single core, need every ounce of performance they can get.
Therefore, some say that C++ is a win for performance reasons, and that is enough to
outweigh all other considerations.  That may be true for the majority of blockchains,
but it is not true for DOT:

- When more computational resources are available, performance is less critical.  DOT should unlock multi-core or cluster-based parallelism.
- Most blockchains' real-time processing is far below what the hardware can handle
- Re-indexing processing speed can be optimized by state checkpoints.

## A word about state

One of the fundamental, firm beliefs about blockchains held by our former CTO is summarized succinctly
as *separation of intent from state*.  This intent is so central that he includes it in the two-sentence
summary of EOS in his
[EOS announcement](https://steemit.com/eos/@dantheman/join-me-at-consensus-2017-for-the-eos-launch-party).

In particular, *state* (expressed as the current set of account balances, market orders, etc.) is a function
of applying *intents* (as expressed by user actions in blocks and transactions).  This function can be changed
-- *even retroactively* -- to have a *different* state result from the *same* stream of intents, as long as the
state still implements the intent.

Separation of intent from state in this way is impossible for a blockchain including user-defined smart contracts.
User-defined state is specified in a smart contract.  The definition of state is expressed as an intent, then state
and intent are no longer independent.  If *different* state results, the intent is no longer implemented.

## Creation of state checkpoints

If state is well-defined, then creation of state checkpoints, and distributing them via trusted out-of-band mechanisms
(for example web-of-trust or hash inclusion in the source code), becomes a real possibility.  State checkpoints
completely solve the reindexing time problem.

A method for incremental state checkpointing is clunkily defined by Ethereum whitepaper's discussion of Patricia trie
data structure.  The paper, "Is Ethereum's Virtual Machine Design Rationale Faulty?", in particular the section, "Can
we eliminate all business logic by including state in all transactions?" also comes close to touching on the issue, but
ends up dismissing the line of thought before it really gets there.

Strong support for high-performance state checkpointing is one of the design problems we should focus on solving with DOT.

## Comparison shopping

Basically the reasons for choosing C# over some other choice (Java, Go, JS, Rust, Python or even Haskell):

- C# has a built-in VM and bytecode interpreter with JIT capability
- C# VM is widely used, multiple implementations, bug-checked
- C# syntax and language design created to be easy to learn, easy to find or train talent
- Compile-time type checking allows powerful IDE's and prevents entire classes of bugs

Java:

- Very similar to C#
- Java is older than C#, C# solves many pain points of Java and is mostly just nicer
- Java has a reputation for security issues

Go / Rust:

- More of a learning curve
- Not as popular, somewhat harder to find talent
- Compiles natively, no VM to leverage

JS / Python:

- Dynamic language, no compile-time checking
- Not as good IDE's
- Popular, easy to find talent
- Good developer productivity
- No accessible VM to leverage
- Low performance

Haskell:

- Huge learning curve
- No in-house experts
- Finding talent difficult

## Conclusion

In conclusion, a strong logical case for C# can be built by following this paper in roughly bottom-to-top order:

- (a) DOT is designed to allow transactions to run in parallel on multiple cores / machines as much as possible.
- (b) A blockchain that allows user-defined smart contracts must have a well-defined notion of state.
- (c) A well-defined notion of state implies that creation of state checkpoints is a realistic goal.
- (d) Creation of state checkpoints solves the reindexing time problem.
- (e) The single-core bottleneck is the first big motivation for obsessing over blockchain performance, but this doesn't matter for DOT; see (a).
- (f) Reindexing time is the second big motivation for obsessing over blockchain performance, but this doesn't matter for DOT; see (b-d).
- (g) Obsessing over blockchain performance is the main technical reason for choosing C++.
- (h) Without a strong technical reason to choose C++, C# is a more natural choice.

