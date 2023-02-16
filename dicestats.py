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
    
    def add(self, probabilities):
        newprob = {}
        
        for value, probability in self.probabilities.items():
            for value2, probability2 in probabilities.items():
                current = value + value2
                
                if not current in newprob.keys():
                    newprob[current] = 0
                
                newprob[current] += probability * probability2
        
        self.probabilities = newprob
    
    def get_probabilities(self):
        return self.probabilities
    
    def print_probabilities(self, precision = 4):
        maxvaluewidth = 0
        
        for value in self.probabilities.keys():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
            
        for value, probability in self.probabilities.items():
            print("{0: >{2}d}: {1:{4}.{3}f}%".format(value, probability * 100, maxvaluewidth, precision, precision + 4))
            
        print()
    
    def plot_probabilities(self, width = 100, barchar = '#'):
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

diceroll = Diceroll()
diceroll.add(Diceroller.rolldice(2, 6))
diceroll.print_probabilities()
diceroll.plot_probabilities()

for i in range(10):
    print(diceroll.roll())
