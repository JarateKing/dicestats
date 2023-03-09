import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import dicestats

# raw 1d4 named "threshold"
rawroll = dicestats.RawDiceroll()
rawroll.apply_probability(dicestats.RawDiceroller.rolldice(1, 4, 'threshold'))

# raw 6d4 named "rolls"
rawroll.apply_probability(dicestats.RawDiceroller.rolldice(6, 4, 'rolls'))

# conversion function
def aboveroll(rawdice):
    # format will be tuples like `(('threshold', (1,)), ('rolls', (1, 1, 1, 1, 1)))`
    
    tobeat = 0
    for dicetype in rawdice:
        if dicetype[0] == 'threshold':
            tobeat = dicetype[1][0]
    
    count = 0
    for dicetype in rawdice:
        if dicetype[0] == 'rolls':
            for roll in dicetype[1]:
                if roll > tobeat:
                    count += 1
    
    return count

# use our conversion function to get the values rolled
diceroll = dicestats.Diceroll()
diceroll.set_probabilities(rawroll.convert_probabilities(dicestats.RawConvert.maxShared))
diceroll.print_probabilities()
diceroll.plot_probabilities(relativeBars = True)
