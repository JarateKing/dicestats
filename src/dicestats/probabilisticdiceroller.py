import random
from .outputformatter import *
from .rawdiceroller import *

class ProbabilisticDiceroller:
	def rolldie(sides, name = ''):
		def internal(sides):
			return [random.randint(1, sides)]
		
		return lambda: {name:internal(sides)}
	
	def rolldice(count, sides, name = ''):
		def internal(count, sides):
			current = []
		
			for i in range(count):
				current.append(random.randint(1, sides))
		
			return current
		
		return lambda: {name:internal(count, sides)}

class ProbabilisticConvert:
    def add(rawdice):
        total = 0
        
        for dicetype in rawdice.values():
            for roll in dicetype:
                total += roll
        
        return total

class ProbabilisticDiceroll:
	def __init__(self):
		self.probabilities = {0: 1.0}
		self.funcs = []
	
	def simulate(self, conversion, numberOfSimulations):
		newprob = {}
		
		for i in range(numberOfSimulations):
			current = {}
			
			for function in self.funcs:
				rolled = function()
				for label, dice in rolled.items():
					if not label in current.keys():
						current[label] = []
					current[label] += dice
			
			converted = conversion(current)
			if not converted in newprob.keys():
				newprob[converted] = 0
			newprob[converted] += 1.0
		
		self.probabilities = {}
		for value, probability in newprob.items():
			self.probabilities[value] = probability / numberOfSimulations
	
	def add(self, function):
		self.funcs.append(function)
	
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
		print("range:	[{0},{1}]".format(minimum, maximum))
		
		mean = 0
		for value, probability in self.probabilities.items():
			mean += value * probability
		print("mean:	 {0:.{1}f}".format(mean, precision))
		
		variance = 0
		for value, probability in self.probabilities.items():
			variance += (value - mean)**2 * probability
		print("variance: {0:.{1}f}".format(variance, precision))
		print("std:	  {0:.{1}f}".format(variance**0.5, precision))
		
		print()
	
	def roll(self):
		choice = random.random()
		
		for value, probability in self.probabilities.items():
			if probability > choice:
				return value
			else:
				choice -= probability
		
		return max(self.probabilities.keys())
