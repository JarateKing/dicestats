import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# raw 10d4
rawroll = dicestats.RawDiceroll()
rawroll.apply_probability(dicestats.RawDiceroller.rolldice(10, 4))

# convert to single values, by counting how many dice share a number
diceroll = rawroll.convert(dicestats.RawConvert.maxShared)
diceroll.print_probabilities()
diceroll.plot_probabilities(relativeBars = True)
