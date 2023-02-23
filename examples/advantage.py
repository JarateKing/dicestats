import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# roll with advantage
advroll = dicestats.Diceroll()
advroll.add(dicestats.Diceroller.advantage(2, 20))

# roll with disadvantage
disroll = dicestats.Diceroll()
disroll.add(dicestats.Diceroller.disadvantage(2, 20))

# print out the chances of each roll
print("ADVANTAGE")
advroll.print_probabilities()
advroll.plot_probabilities()

print("DISADVANTAGE")
disroll.print_probabilities()
disroll.plot_probabilities()
