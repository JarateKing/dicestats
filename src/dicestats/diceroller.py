import random
from .outputformatter import *
from .rawdiceroller import *

class Diceroller:
    def rolldie(sides):
        probabilities = {}
        
        for i in range(sides):
            current = i + 1
            probabilities[current] = 1 / sides
        
        return probabilities
    
    def rolldice(count, sides):
        probabilities = {0: 1.0}
        powerbilities = Diceroller.rolldie(sides)
        
        # binary exponentiation
        while (count > 0):
            if (count % 2):
                newprob = {}
                for value, probability in probabilities.items():
                    for value2, probability2 in powerbilities.items():
                        current = value + value2
                        if not current in newprob.keys():
                            newprob[current] = 0
                        newprob[current] += probability * probability2
                probabilities = newprob
            
            newprob = {}
            for value, probability in powerbilities.items():
                for value2, probability2 in powerbilities.items():
                    current = value + value2
                    if not current in newprob.keys():
                        newprob[current] = 0
                    newprob[current] += probability * probability2
            powerbilities = newprob
            
            count = count // 2
        
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
    
    def penetratingdice(count, sides, recursiveDepth = 0, probabilityLimit = 0):
        # get exploded probabilities
        explodedProbabilities = {}
        offset = 0
        runningProbability = 1
        
        if probabilityLimit != 0:
            recursiveDepth = 1000
        
        # if we roll more than the number of sides, everything will be 0
        torepeat = sides
        if recursiveDepth != 0:
            torepeat = min(torepeat, recursiveDepth)
        
        for r in range(torepeat):
            for i in range(sides):
                current = max(offset + i + 1 - r, offset)
                probability = 1 / sides * runningProbability
                
                if (i + 1) != sides:
                    if not current in explodedProbabilities.keys():
                        explodedProbabilities[current] = 0
                        
                    explodedProbabilities[current] += probability
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
    
    def advantage(count, sides):
        probabilities = {0: 1.0}
        
        for i in range(count):
            newprob = {}
            
            for value, probability in probabilities.items():
                for value2, probability2 in Diceroller.rolldie(sides).items():
                    current = max(value, value2)
                    
                    if not current in newprob.keys():
                        newprob[current] = 0
                    
                    newprob[current] += probability * probability2
            
            probabilities = newprob.copy()
        
        return probabilities
    
    def disadvantage(count, sides):
        probabilities = {0: 1.0}
        
        if count > 0:
            probabilities = Diceroller.rolldie(sides)
        
        for i in range(count - 1):
            newprob = {}
            
            for value, probability in probabilities.items():
                for value2, probability2 in Diceroller.rolldie(sides).items():
                    current = min(value, value2)
                    
                    if not current in newprob.keys():
                        newprob[current] = 0
                    
                    newprob[current] += probability * probability2
            
            probabilities = newprob.copy()
        
        return probabilities
    
    def highest(count, sides, toKeep):
        # TODO: refactor and optimize
        raw = RawDiceroll()
        raw.apply_probability(RawDiceroller.rolldice(count, sides))
        
        def highestConverter(rawdice):
            count = 0
            
            for dicetype in rawdice:
                for i, roll in enumerate(dicetype[1]):
                    if i > len(dicetype[1]) - toKeep - 1:
                        count += roll
            return count
        
        return raw.convert_probabilities(highestConverter)
    
    def lowest(count, sides, toKeep):
        # TODO: refactor and optimize
        raw = RawDiceroll()
        raw.apply_probability(RawDiceroller.rolldice(count, sides))
        
        def lowestConverter(rawdice):
            count = 0
            
            for dicetype in rawdice:
                for i, roll in enumerate(dicetype[1]):
                    if i < toKeep:
                        count += roll
            return count
        
        return raw.convert_probabilities(lowestConverter)

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
        print_output(self.probabilities, True, True, False, precision = precision)
    
    def print_at_least(self, precision = 4):
        self.__sort_probabilities()
        print_output(self.probabilities, True, True, False, precision = precision, comparisonType = comparison.AT_LEAST)
    
    def print_at_most(self, precision = 4):
        self.__sort_probabilities()
        print_output(self.probabilities, True, True, False, precision = precision, comparisonType = comparison.AT_MOST)
    
    def print_less_than(self, precision = 4):
        self.__sort_probabilities()
        print_output(self.probabilities, True, True, False, precision = precision, comparisonType = comparison.LESS_THAN)
    
    def print_more_than(self, precision = 4):
        self.__sort_probabilities()
        print_output(self.probabilities, True, True, False, precision = precision, comparisonType = comparison.MORE_THAN)
    
    def plot_probabilities(self, width = 100, barchar = '#', relativeBars = False):
        self.__sort_probabilities()
        print_output(self.probabilities, True, False, True, width = width, barchar = barchar, relativeBars = relativeBars)
    
    def plot_at_least(self, width = 100, barchar = '#', relativeBars = False):
        self.__sort_probabilities()
        print_output(self.probabilities, True, False, True, width = width, barchar = barchar, relativeBars = relativeBars, comparisonType = comparison.AT_LEAST)
    
    def plot_at_most(self, width = 100, barchar = '#', relativeBars = False):
        self.__sort_probabilities()
        print_output(self.probabilities, True, False, True, width = width, barchar = barchar, relativeBars = relativeBars, comparisonType = comparison.AT_MOST)
    
    def plot_less_than(self, width = 100, barchar = '#', relativeBars = False):
        self.__sort_probabilities()
        print_output(self.probabilities, True, False, True, width = width, barchar = barchar, relativeBars = relativeBars, comparisonType = comparison.LESS_THAN)
    
    def plot_more_than(self, width = 100, barchar = '#', relativeBars = False):
        self.__sort_probabilities()
        print_output(self.probabilities, True, False, True, width = width, barchar = barchar, relativeBars = relativeBars, comparisonType = comparison.MORE_THAN)
    
    def print_statistics(self, precision = 4):
        minimum = 0
        minimumSet = False
        maximum = 0
        maximumSet = False
        for value, probability in self.probabilities.items():
            if minimumSet:
                minimum = min(minimum, value)
            else:
                minimum = value
                minimumSet = True
            if maximumSet:
                maximum = max(maximum, value)
            else:
                maximum = value
                maximumSet = True
        print("range:    [{0},{1}]".format(minimum, maximum))
        
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
