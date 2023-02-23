import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# setup our diceroll
diceroll = dicestats.Diceroll()

# roll 3d6
diceroll.add(dicestats.Diceroller.rolldice(3, 6))

# roll the dice 6 times
for i in range(6):
    print(diceroll.roll())
