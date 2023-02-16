import os

class Diceroll:
    def __init__(self):
        self.probabilities = {0: 1.0}
    
    def rolldie(self, sides):
        newprob = {}
        
        for value, probability in self.probabilities.items():
            for i in range(sides):
                current = value + i + 1
                
                if not current in newprob.keys():
                    newprob[current] = (1 / sides)
                else:
                    newprob[current] += probability * (1 / sides)
        
        self.probabilities = newprob
    
    def rolldice(self, count, sides):
        for i in range(count):
            self.rolldie(sides)
    
    def get_probabilities(self):
        return self.probabilities
    
    def print_probabilities(self):
        maxvaluewidth = 0
        
        for value in self.probabilities.keys():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
            
        for value, probability in self.probabilities.items():
            print("{0: >{2}d}: {1:.4f}%".format(value, probability * 100, maxvaluewidth))
            
        print()

diceroll = Diceroll()
diceroll.rolldice(1, 6)
diceroll.print_probabilities()

diceroll = Diceroll()
diceroll.rolldice(2, 6)
diceroll.print_probabilities()