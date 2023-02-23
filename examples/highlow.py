import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# roll highest 3 of 6d6
advroll = dicestats.Diceroll()
advroll.add(dicestats.Diceroller.highest(6, 6, 3))

# roll lowest 3 of 6d6
disroll = dicestats.Diceroll()
disroll.add(dicestats.Diceroller.lowest(6, 6, 3))

# print out the chances of each roll
print("HIGHEST 3")
advroll.print_probabilities()
advroll.plot_probabilities()

print("LOWEST 3")
disroll.print_probabilities()
disroll.plot_probabilities()
