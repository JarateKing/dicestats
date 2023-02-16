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
    
    def print_probabilities(self):
        print(self.probabilities)

diceroll = Diceroll()
diceroll.rolldice(2, 6)
diceroll.print_probabilities()
