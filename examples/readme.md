# Examples

Included in this folder are various examples for usage of dicestats.

## basic.py

This is the simplest example of dicestats being used. It rolls 3d6 and prints the probabilities as well as plots them.

## raw.py

This is the raw diceroller's equivalent for `basic.py`. It also rolls 3d6 and prints the probabilities / plots them, but it preserves the individual dice rolled. In particular, where the regular diceroller in `basic.py` would count a roll of `1,1,3` and `1,2,2` as the same (since both add up to `5`) the raw diceroller will count them as distinct rolls.
