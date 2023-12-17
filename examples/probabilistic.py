import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# setup our diceroll
diceroll = dicestats.ProbabilisticDiceroll()

# roll 3d6
diceroll.add(dicestats.ProbabilisticDiceroller.rolldice(3, 6))

# run simulator
diceroll.simulate(1000000)

# print out the chances
diceroll.print_probabilities()
diceroll.plot_probabilities()
