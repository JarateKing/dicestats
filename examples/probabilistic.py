import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# setup our diceroll
diceroll = dicestats.ProbabilisticDiceroll()

# roll 3d6
diceroll.add(dicestats.ProbabilisticDiceroller.rolldice(10, 20))

# simulate 100k rolls
diceroll.simulate(dicestats.ProbabilisticConvert.add, 100000)

# print out the chances
diceroll.print_probabilities()
diceroll.plot_probabilities()
