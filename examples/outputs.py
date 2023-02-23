import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# setup our diceroll
diceroll = dicestats.Diceroll()

# roll 3d6
diceroll.add(dicestats.Diceroller.rolldice(3, 6))

# print out combined output
dicestats.print_output(diceroll.get_probabilities(), True, True, True)

# plot other forms of graphs
print("AT MOST")
diceroll.plot_at_most()
print("AT LEAST")
diceroll.plot_at_least()
print("LESS THAN")
diceroll.plot_less_than()
print("MORE THAN")
diceroll.plot_more_than()

# print statistical information
diceroll.print_statistics()
