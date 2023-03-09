import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# roll for each player
rawroll = dicestats.RawDiceroll()
rawroll.apply_probability(dicestats.RawDiceroller.rolldice(1, 6, 'Player 1'))
rawroll.apply_probability(dicestats.RawDiceroller.rolldice(1, 6, 'Player 2'))
rawroll.apply_probability(dicestats.RawDiceroller.rolldice(1, 6, 'Player 3'))

# check what turn orders are most likely
diceroll = dicestats.Diceroll()
diceroll.set_probabilities(rawroll.convert_probabilities(dicestats.RawConvert.goFirst))
diceroll.print_probabilities()
diceroll.plot_probabilities(relativeBars = True)
