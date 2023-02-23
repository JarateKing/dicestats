import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# roll 2d4 (each explodes on 4, minus 1 for each additional roll)
diceroll = dicestats.Diceroll()
diceroll.add(dicestats.Diceroller.penetratingdice(2, 4))
diceroll.print_probabilities()
diceroll.plot_probabilities(relativeBars = True)
