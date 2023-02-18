# Dicestats

A utility for getting and manipulating probability distributions of dice rolls.

## Basic Usage

The only dependency required is [Python 3](https://www.python.org/downloads/).

We can create a simple program to make use of dicestats:

<details><summary>example.py</summary>
```python
import dicestats

# setup our diceroll
diceroll = dicestats.Diceroll()

# roll 2d6
diceroll.add(dicestats.Diceroller.rolldice(2, 6))

# print out the chances of each roll
diceroll.print_probabilities()
```
</details>

Running this program with `python ./example.py` should give us the output:

<details><summary>example.py output</summary>
```
 2:   2.7778%
 3:   5.5556%
 4:   8.3333%
 5:  11.1111%
 6:  13.8889%
 7:  16.6667%
 8:  13.8889%
 9:  11.1111%
10:   8.3333%
11:   5.5556%
12:   2.7778%

 2: ###
 3: ######
 4: ########
 5: ###########
 6: ##############
 7: #################
 8: ##############
 9: ###########
10: ########
11: ######
12: ###
```
</details>

See the [examples](/examples) for more details on usage.

## Motivation

For anyone familiar with [anydice.com](https://anydice.com/), they'll notice that this fulfills a similar function. However, there are some key differences:

* dicestats is a commandline utility that doesn't require an internet connection
* anydice has an upper limit on computation-time for very large queries (which makes sense, considering it's a web service). Dicestats has no restriction
* functions are written in python rather than in anydice's own language. While this can be more cumbersome for simple queries, it should be a more natural environment for complex functions for people familiar with python
* in addition to the anydice-style diceroller, dicestats provides a raw diceroller that keeps each possible individual diceroll preserved
