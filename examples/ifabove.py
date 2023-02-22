import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# roll 1d6 and only count above 3
individualroll = dicestats.Diceroll()
individualroll.add(dicestats.Diceroller.rolldie(6))
individualroll.apply_function(lambda x: x if x > 3 else 0)

# 6d6 above 3 by applying the above probability 6 times
diceroll = dicestats.Diceroll()
for i in range(6):
    diceroll.add(individualroll.get_probabilities())
diceroll.print_probabilities()
