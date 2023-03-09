import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# raw 10d4
rawroll = dicestats.RawDiceroll()
rawroll.apply_probability(dicestats.RawDiceroller.rolldice(10, 4))

# convert to single values, by counting how many dice share a number
diceroll.print_probabilities()
diceroll = dicestats.Diceroll()
diceroll.set_probabilities(rawroll.convert_probabilities(dicestats.RawConvert.maxShared))
diceroll.plot_probabilities(relativeBars = True)
