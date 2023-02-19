import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# setup our dicerolls
diceroll = dicestats.Diceroll()
multroll = dicestats.Diceroll()

# partial: 3d6 - 2d4
diceroll.add(dicestats.Diceroller.rolldice(3, 6))
diceroll.subtract(dicestats.Diceroller.rolldice(2, 4))

# partial: 3d2 * 2
multroll.add(dicestats.Diceroller.rolldice(3, 2))
multroll.multiply_constant(2)

# (3d6 + 2d4) + (3d2 * 2) + 5
diceroll.add(multroll.get_probabilities())
diceroll.add_constant(5)

# print out the chances of each roll
diceroll.print_probabilities()
diceroll.plot_probabilities()
