
# Reference resolving

## Dependencies

### slither 

```sh
pipx install slither-analyzer
```

## Installation

```sh
npm i
```

## Main

This repository illustrates slither unable to resolve references across
compilation units. Contract `A` is designated as `>=0.8.0`, contract `B` as
`0.8.0`, contract C as `0.8.1`. It follows the compilation units will be

* A, B
* A, C

Woke correctly shows that `a_main` is called in `b_main` and `c_main`:

![woke graph](https://github.com/hacker-dom/reference-resolving/blob/main/assets/woke-graph.png?raw=true)

and this behavior persists into the Api (todo: show)

However, when using Slither Api (eg for detectors), multiple `Contract`
instances will exist in `Slither.contracts` for each contract that spans
multiple compilation units. This leads to bug that can be illustrated by running
`python example_slither.py`:

```sh
$ python example_slither.py
Printing derived contracts of A
[<slither.core.declarations.contract.Contract object at 0x105ee86a0>]
Printing name of above derived contract
C
Printing references of A.a_main
[]
```

As we can see, only C is viewed as a derived contract of A.

Tested on:
- `slither-analyzer==0.9.6`
- `woke==3.5.0`
