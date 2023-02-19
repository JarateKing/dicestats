import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# roll 2d4 (each explodes on 4)
diceroll = dicestats.Diceroll()
diceroll.add(dicestats.Diceroller.explodingdice(2, 4))
diceroll.plot_probabilities(relativeBars = True)

# roll 2d4 (each explodes on 4) with recursive limit
diceroll = dicestats.Diceroll()
diceroll.add(dicestats.Diceroller.explodingdice(2, 4, recursiveDepth = 5))
diceroll.plot_probabilities(relativeBars = True)

# roll 2d4 (each explodes on 4) with probability limit
diceroll = dicestats.Diceroll()
diceroll.add(dicestats.Diceroller.explodingdice(2, 4, probabilityLimit = 0.001))
diceroll.plot_probabilities(relativeBars = True)
