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
    
    def print_probabilities(self, precision = 4):
        self.__sort_probabilities()
        maxvaluewidth = 0
        
        for value in self.probabilities.keys():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
            
        for value, probability in self.probabilities.items():
            print("{0: >{2}d}: {1:{4}.{3}f}%".format(value, probability * 100, maxvaluewidth, precision, precision + 4))
            
        print()
    
    def plot_probabilities(self, width = 100, barchar = '#'):
        self.__sort_probabilities()
        maxvaluewidth = 0
        
        for value in self.probabilities.keys():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
        
        for value, probability in self.probabilities.items():
            barstr = barchar * round(probability * 100 / (100 / width))
            print("{0: >{1}d}:".format(value, maxvaluewidth), barstr)
        
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
    
    def plot_probabilities(self, width = 100, barchar = '#'):
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
            barstr = barchar * round(probability * 100 / (100 / width))
            print("{0:<{2}}:".format(line, probability * 100, maxlinewidth), barstr)
        print()
    
    def get_probabilities(self):
        return self.probabilities

diceroll = RawDiceroll()
diceroll.apply_probability(RawDiceroller.rolldie(2, 'd2'))
diceroll.apply_probability(RawDiceroller.rolldice(3, 2, 'd2'))
diceroll.apply_probability(RawDiceroller.rolldice(1, 4, 'd4'))
diceroll.print_probabilities()
diceroll.plot_probabilities()
