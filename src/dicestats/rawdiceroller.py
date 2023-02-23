import random
from .diceroller import *

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
    
    def __get_label_overrides(self):
        lines = {}
        
        for value, probability in self.probabilities.items():
            line = ' '.join(map(lambda x: '"' + str(x[0]) + '"=' + ','.join(map(lambda x: str(x), x[1])), value))
            lines[value] = line
        
        return lines
    
    def print_probabilities(self, precision = 4):
        lines = self.__get_label_overrides()
        print_output(self.probabilities, True, True, False, labelOverrides = lines, precision = precision)
    
    def plot_probabilities(self, width = 100, barchar = '#', relativeBars = False):
        lines = self.__get_label_overrides()
        print_output(self.probabilities, True, False, True, labelOverrides = lines, width = width, barchar = barchar, relativeBars = relativeBars)
    
    def get_probabilities(self):
        return self.probabilities
    
    def convert_probabilities(self, function):
        newprob = {}
        
        for value, probability in self.probabilities.items():
            current = function(value)
            
            if not current in newprob.keys():
                newprob[current] = 0
                
            newprob[current] += probability
        return newprob
    
    def convert(self, function):
        toret = Diceroll()
        toret.set_probabilities(self.convert_probabilities(function))
        return toret
