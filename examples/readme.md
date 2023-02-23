# Examples

Included in this folder are various examples for usage of dicestats.

## basic.py

This is the simplest example of dicestats being used. It rolls 3d6 and prints the probabilities as well as plots them.

## outputs.py

In this example we show some of the options available for outputting the probabilities of rolls.

## roll.py

This example shows obtaining a random result from the diceroll probability distribution, effectively serving as a traditional diceroller.

## raw.py

This is the raw diceroller's equivalent for `basic.py`. It also rolls 3d6 and prints the probabilities / plots them, but it preserves the individual dice rolled. In particular, where the regular diceroller in `basic.py` would count a roll of `1,1,3` and `1,2,2` as the same (since both add up to `5`) the raw diceroller will count them as distinct rolls.

## mixed.py

This example demonstrates a more complex dice expression, `3d6 - 2d4 + (3d2 * 2) + 5` which involves adding multiple dice together in a single roll, doing a separate roll and multiplying that before merging it into the other dice roll, and dealing with constants.

## advantage.py

In this example we show rolling with advantage and disadvantage, or rolling twice and taking the highest roll with advantage and the lowest roll with disadvantage.

## highlow.py

This example demonstrates the generalization of advantage and disadvantage, where we take multiple of the highest or lowest values and add them together. In particular, we take the highest 3 of 6d6 and the lowest 3 of 6d6.

## exploding.py

An example of exploding dice (dice that when they roll maximum, you reroll them and add the results together, potentially repeating this again each time you roll maximum). Specifically, we roll `2d4` and explode each dice individually when they roll `4`. Because technically any arbitrarily high number could be rolled (though it becomes very unlikely) we also show off different ways to set limits -- by default, dice will only explode up to `10` times. We show manually setting that limit to `5`, and we show another method of limiting it by cutting it off after we're dealing with probabilities below `0.001`.

## commoncount.py

This example shows using the raw diceroller and interpreting the results of the dice in a unique way. Specifically, we roll `10d4` and then analyze the individual rolls to see how many have the same roll as each other. For example, if we rolled `1,1,1,2,2,3,3,3,3,4` we would get the result `4`, since `4` dice share the same number (the `4` rolls of `3`).

## ifabove.py

With this example we show two things:

- the use of `apply_function` for doing arbitrary modifications on the roll values. In particular, we apply `lambda x: x if x > 3 else 0` so that rolls of of `1`, `2`, or `3` become 0 instead.
- we use one diceroll to obtain a certain probability and then we combine multiple of that diceroll together. This technique allows us to compose fairly elaborate rolls together.

## ifabove2.py

This example focuses on a fairly interesting mechanic: roll 1d4 for the "threshold", and then roll 6d4 and count the number of rolls above the threshold. To do this, we'll use raw dicerolls, with some additional features:

- even though all the dicerolls go through the same RawDiceroll object, we name them the threshold die and the roll dice to distinguish them from each other.
- we write a custom convert function to interpret the raw dicerolls and apply our custom mechanic
