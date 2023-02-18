import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# setup our diceroll
diceroll = dicestats.RawDiceroll()

# roll 3d6
diceroll.apply_probability(dicestats.RawDiceroller.rolldice(3, 6))

# print out the chances of each roll
diceroll.print_probabilities()
diceroll.plot_probabilities()
