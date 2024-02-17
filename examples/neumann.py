import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# two coinflips
# label the first "1" and the second "2" to keep the right order
rawroll = dicestats.RawDiceroll()
rawroll.apply_probability(dicestats.RawDiceroller.rolldice(1, 2, '1'))
rawroll.apply_probability(dicestats.RawDiceroller.rolldice(1, 2, '2'))

# use the first result if both results are different
# result is 0 otherwise, if they are the same
def neumann(rawdice):
	a = rawdice[0][1][0]
	b = rawdice[1][1][0]
	
	if (a == b):
		return 0
	
	return a

# use our conversion function to get the values rolled
diceroll = dicestats.Diceroll()
diceroll.set_probabilities(rawroll.convert_probabilities(neumann))
diceroll.print_probabilities()
