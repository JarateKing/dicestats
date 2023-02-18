# Dicestats

A utility for getting and manipulating probability distributions of dice rolls.

## Basic Usage

The only dependency required is [Python 3](https://www.python.org/downloads/).

## Motivation

For anyone familiar with [anydice.com](https://anydice.com/), they'll notice that this fulfills a similar function. However, there are some key differences:

* dicestats is a commandline utility that doesn't require an internet connection
* anydice has an upper limit on computation-time for very large queries (which makes sense, considering it's a web service). Dicestats has no restriction
* functions are written in python rather than in anydice's own language. While this can be more cumbersome for simple queries, it should be a more natural environment for complex functions for people familiar with python
* in addition to the anydice-style diceroller, dicestats provides a raw diceroller that keeps each possible individual diceroll preserved
