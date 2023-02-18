import random

class Diceroller:
    def rolldie(sides):
        probabilities = {}
        
        for i in range(sides):
            current = i + 1
            probabilities[current] = 1 / sides
        
        return probabilities
    
    def rolldice(count, sides):
        probabilities = {0: 1.0}
        
        for i in range(count):
            newprob = {}
            
            for value, probability in probabilities.items():
                for value2, probability2 in Diceroller.rolldie(sides).items():
                    current = value + value2
                    
                    if not current in newprob.keys():
                        newprob[current] = 0
                    
                    newprob[current] += probability * probability2
            
            probabilities = newprob.copy()
        
        return probabilities
    
    def explodingdice(count, sides, recursiveDepth = 10, probabilityLimit = 0):
        # get exploded probabilities
        explodedProbabilities = {}
        offset = 0
        runningProbability = 1
        
        if probabilityLimit != 0:
            recursiveDepth = 1000
        
        for r in range(recursiveDepth):
            for i in range(sides):
                current = offset + i + 1
                probability = 1 / sides * runningProbability
                
                if (i + 1) != sides:
                    explodedProbabilities[current] = probability
                else:
                    offset = current
                    runningProbability = probability
                
                if runningProbability <= probabilityLimit:
                    break
            if runningProbability <= probabilityLimit:
                break
        
        # apply exploded probabilities with rolls
        probabilities = {0: 1.0}
        for i in range(count):
            newprob = {}
            
            for value, probability in probabilities.items():
                for value2, probability2 in explodedProbabilities.items():
                    current = value + value2
                    
                    if not current in newprob.keys():
                        newprob[current] = 0
                    
                    newprob[current] += probability * probability2
            
            probabilities = newprob.copy()
        
        return probabilities

class Diceroll:
    def __init__(self):
        self.probabilities = {0: 1.0}
    
    def apply_probability(self, probabilities, function):
        newprob = {}
        
        for value, probability in self.probabilities.items():
            for value2, probability2 in probabilities.items():
                current = function(value, value2)
                
                if not current in newprob.keys():
                    newprob[current] = 0
                
                newprob[current] += probability * probability2
        
        self.probabilities = newprob
    
    def add(self, probabilities):
        self.apply_probability(probabilities, lambda x, y: x + y)
    
    def subtract(self, probabilities):
        self.apply_probability(probabilities, lambda x, y: x - y)
    
    def multiply(self, probabilities):
        self.apply_probability(probabilities, lambda x, y: x * y)
    
    def apply_function(self, function):
        newprob = {}
        
        for value, probability in self.probabilities.items():
            current = function(value)
                
            if not current in newprob.keys():
                newprob[current] = 0
                
            newprob[current] += probability
        
        self.probabilities = newprob
    
    def add_constant(self, constant):
        self.apply_function(lambda x: x + constant)
    
    def subtract_constant(self, constant):
        self.apply_function(lambda x: x - constant)
        
    def multiply_constant(self, constant):
        self.apply_function(lambda x: x * constant)
    
    def __sort_probabilities(self):
        self.probabilities = dict(sorted(self.probabilities.items()))
    
    def get_probabilities(self):
        self.__sort_probabilities()
        return self.probabilities
    
    def set_probabilities(self, probabilities):
        self.probabilities = probabilities
        self.__sort_probabilities()
    
    def print_probabilities(self, precision = 4):
        self.__sort_probabilities()
        maxvaluewidth = 0
        
        for value in self.probabilities.keys():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
            
        for value, probability in self.probabilities.items():
            print("{0: >{2}d}: {1:{4}.{3}f}%".format(value, probability * 100, maxvaluewidth, precision, precision + 4))
            
        print()
    
    def print_at_least(self, precision = 4):
        self.__sort_probabilities()
        maxvaluewidth = 0
        
        for value in self.probabilities.keys():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
        
        current = 1
        for value, probability in self.probabilities.items():
            print("{0: >{2}d}: {1:{4}.{3}f}%".format(value, current * 100, maxvaluewidth, precision, precision + 4))
            current -= probability
        
        print()
    
    def print_at_most(self, precision = 4):
        self.__sort_probabilities()
        maxvaluewidth = 0
        
        for value in self.probabilities.keys():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
        
        current = 0
        for value, probability in self.probabilities.items():
            current += probability
            print("{0: >{2}d}: {1:{4}.{3}f}%".format(value, current * 100, maxvaluewidth, precision, precision + 4))
        
        print()
    
    def print_less_than(self, precision = 4):
        self.__sort_probabilities()
        maxvaluewidth = 0
        
        for value in self.probabilities.keys():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
        
        current = 0
        for value, probability in self.probabilities.items():
            print("{0: >{2}d}: {1:{4}.{3}f}%".format(value, current * 100, maxvaluewidth, precision, precision + 4))
            current += probability
        
        print()
    
    def print_more_than(self, precision = 4):
        self.__sort_probabilities()
        maxvaluewidth = 0
        
        for value in self.probabilities.keys():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
        
        current = 1
        for value, probability in self.probabilities.items():
            current -= probability
            print("{0: >{2}d}: {1:{4}.{3}f}%".format(value, current * 100, maxvaluewidth, precision, precision + 4))
        
        print()
    
    def plot_probabilities(self, width = 100, barchar = '#', relativeBars = False):
        self.__sort_probabilities()
        maxvaluewidth = 0
        maxpercent = 0
        
        for value, probability in self.probabilities.items():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
            maxpercent = max(maxpercent, probability * 100)
        
        for value, probability in self.probabilities.items():
            barstr = barchar * round(probability * 100 / ((maxpercent if relativeBars else 100) / width))
            print("{0: >{1}d}:".format(value, maxvaluewidth), barstr)
        
        print()
    
    def plot_at_least(self, width = 100, barchar = '#', relativeBars = False):
        self.__sort_probabilities()
        maxvaluewidth = 0
        
        for value, probability in self.probabilities.items():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
        
        current = 1
        for value, probability in self.probabilities.items():
            barstr = barchar * round(current * 100 / (100 / width))
            current -= probability
            print("{0: >{1}d}:".format(value, maxvaluewidth), barstr)
        
        print()
    
    def plot_at_most(self, width = 100, barchar = '#', relativeBars = False):
        self.__sort_probabilities()
        maxvaluewidth = 0
        maxpercent = 100
        
        for value, probability in self.probabilities.items():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
        
        current = 0
        for value, probability in self.probabilities.items():
            current += probability
            barstr = barchar * round(current * 100 / (100 / width))
            print("{0: >{1}d}:".format(value, maxvaluewidth), barstr)
        
        print()
    
    def plot_less_than(self, width = 100, barchar = '#', relativeBars = False):
        self.__sort_probabilities()
        maxvaluewidth = 0
        maxpercent = 0
        
        current = 0
        for value, probability in self.probabilities.items():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
            maxpercent = max(maxpercent, current * 100)
            current += probability
        
        current = 0
        for value, probability in self.probabilities.items():
            barstr = barchar * round(current * 100 / ((maxpercent if relativeBars else 100) / width))
            current += probability
            print("{0: >{1}d}:".format(value, maxvaluewidth), barstr)
        
        print()
    
    
    def print_statistics(self, precision = 4):
        mean = 0
        for value, probability in self.probabilities.items():
            mean += value * probability
        print("mean:     {0:.{1}f}".format(mean, precision))
        
        variance = 0
        for value, probability in self.probabilities.items():
            variance += (value - mean)**2 * probability
        print("variance: {0:.{1}f}".format(variance, precision))
        print("std:      {0:.{1}f}".format(variance**0.5, precision))
        
        print()
    
    def roll(self):
        choice = random.random()
        
        for value, probability in self.probabilities.items():
            if probability > choice:
                return value
            else:
                choice -= probability
        
        return max(self.probabilities.keys())

class RawDiceroller:
    def rolldie(sides, name = ''):
        probabilities = {}
        
        for i in range(sides):
            current = i + 1
            probabilities[((name, (current,)),)] = 1 / sides
        
        return probabilities
    
    def rolldice(count, sides, name = ''):
        probabilities = {(): 1.0}
        
        for i in range(count):
            newprob = {}
            
            for value, probability in probabilities.items():
                for value2, probability2 in RawDiceroller.rolldie(sides, name).items():
                    current = value
                    
                    toadd = ()
                    # get the rolls to add
                    for val in value2:
                        if val[0] == name:
                            toadd = val[1]
                    
                    # ensure that the name exists in the tuple
                    valueExists = False
                    for val in value:
                        if val[0] == name:
                            valueExists = True
                    if not valueExists:
                        current = value + ((name, ()),)
                    
                    # add roll to that name's tuple
                    current = list(current)
                    for j in range(len(current)):
                        val = current[j]
                        if val[0] == name:
                            current[j] = (name, tuple(sorted(val[1] + toadd)))
                    current = tuple(sorted(current))
                    
                    if not current in newprob.keys():
                        newprob[current] = 0
                    
                    newprob[current] += probability * probability2
            
            probabilities = newprob.copy()
        
        return probabilities

class RawConvert:
    def add(rawdice):
        total = 0
        
        for dicetype in rawdice:
            for roll in dicetype[1]:
                total += roll
        
        return total
    
    def maximum(rawdice):
        highest = 0
        highestSet = False
        
        for dicetype in rawdice:
            for roll in dicetype[1]:
                if highestSet:
                    highest = max(highest, roll)
                else:
                    highest = roll
                    highestSet = True
        
        return highest
    
    def minimum(rawdice):
        lowest = 0
        lowestSet = False
        
        for dicetype in rawdice:
            for roll in dicetype[1]:
                if lowestSet:
                    lowest = min(lowest, roll)
                else:
                    lowest = roll
                    lowestSet = True
        
        return lowest
    
    def maxShared(rawdice):
        rollcounts = {}
        
        for dicetype in rawdice:
            for roll in dicetype[1]:
                if not roll in rollcounts.keys():
                    rollcounts[roll] = 0
                    
                rollcounts[roll] += 1
        
        best = 0
        for value in rollcounts.values():
            best = max(best, value)
        
        return best

class RawDiceroll:
    def __init__(self):
        self.probabilities = {(): 1.0}
    
    def apply_probability(self, probabilities):
        newprob = {}
        
        for value, probability in self.probabilities.items():
            for value2, probability2 in probabilities.items():
                for name in map(lambda x: x[0], value2):
                    current = value
                    
                    toadd = ()
                    # get the rolls to add
                    for val in value2:
                        if val[0] == name:
                            toadd = val[1]
                    
                    # ensure that the name exists in the tuple
                    valueExists = False
                    for val in value:
                        if val[0] == name:
                            valueExists = True
                    if not valueExists:
                        current = value + ((name, ()),)
                    
                    # add roll to that name's tuple
                    current = list(current)
                    for j in range(len(current)):
                        val = current[j]
                        if val[0] == name:
                            current[j] = (name, tuple(sorted(val[1] + toadd)))
                    current = tuple(sorted(current))
                    
                    if not current in newprob.keys():
                        newprob[current] = 0
                    
                    newprob[current] += probability * probability2
        
        self.probabilities = newprob
    
    def print_probabilities(self, precision = 4):
        maxlinewidth = 0
        lines = {}
        
        # build dict of lines
        for value, probability in self.probabilities.items():
            line = ' '.join(map(lambda x: '"' + str(x[0]) + '"=' + ','.join(map(lambda x: str(x), x[1])), value))
            lines[line] = probability
        
        # get maximum size for formatting purposes
        for line in lines.keys():
            maxlinewidth = max(maxlinewidth, len(line))
            
        # print
        for line, probability in lines.items():
            print("{0:<{2}}: {1:{4}.{3}f}%".format(line, probability * 100, maxlinewidth, precision, precision + 4))
        print()
    
    def plot_probabilities(self, width = 100, barchar = '#', relativeBars = False):
        maxlinewidth = 0
        maxpercent = 0
        lines = {}
        
        # build dict of lines
        for value, probability in self.probabilities.items():
            line = ' '.join(map(lambda x: '"' + str(x[0]) + '"=' + ','.join(map(lambda x: str(x), x[1])), value))
            lines[line] = probability
            maxlinewidth = max(maxlinewidth, len(line))
            maxpercent = max(maxpercent, probability * 100)
            
        # print
        for line, probability in lines.items():
            barstr = barchar * round(probability * 100 / ((maxpercent if relativeBars else 100) / width))
            print("{0:<{2}}:".format(line, probability * 100, maxlinewidth), barstr)
        print()
    
    def get_probabilities(self):
        return self.probabilities
    
    def convert(self, function):
        newprob = {}
        
        for value, probability in self.probabilities.items():
            current = function(value)
            
            if not current in newprob.keys():
                newprob[current] = 0
                
            newprob[current] += probability
        
        toret = Diceroll()
        toret.set_probabilities(newprob)
        return toret

diceroll = RawDiceroll()
diceroll.apply_probability(RawDiceroller.rolldice(4, 4))
diceroll.apply_probability(RawDiceroller.rolldice(3, 6))
diceroll.apply_probability(RawDiceroller.rolldice(2, 10))
diceroll = diceroll.convert(RawConvert.maxShared)
diceroll.print_probabilities()
diceroll.plot_probabilities(relativeBars = True)
diceroll.print_at_least()
diceroll.plot_at_least(relativeBars = True)
diceroll.print_at_most()
diceroll.plot_at_most(relativeBars = True)
diceroll.print_less_than()
diceroll.plot_less_than(relativeBars = True)
diceroll.print_more_than()
