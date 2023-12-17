import random
from .outputformatter import *
from .rawdiceroller import *

class ProbabilisticDiceroller:
	def rolldie(sides):
		def internal(sides):
			return random.randint(1, sides)
		
		return lambda: internal(sides)
	
	def rolldice(count, sides):
		def internal(count, sides):
			current = 0
		
			for i in range(count):
				current += random.randint(1, sides)
		
			return current
		
		return lambda: internal(count, sides)
	
	def explodingdice(count, sides, recursiveDepth = 10, probabilityLimit = 0):
		return lambda: 0
	
	def penetratingdice(count, sides, recursiveDepth = 0, probabilityLimit = 0):
		return lambda: 0
	
	def advantage(count, sides):
		return lambda: 0
	
	def disadvantage(count, sides):
		return lambda: 0
	
	def highest(count, sides, toKeep):
		return lambda: 0
	
	def lowest(count, sides, toKeep):
		return lambda: 0

class ProbabilisticDiceroll:
	def __init__(self):
		self.probabilities = {0: 1.0}
		self.funcs = []
	
	def simulate(self, numberOfSimulations):
		newprob = {}
	
		for i in range(numberOfSimulations):
			current = 0
			for (probfunc, appliedfunc) in self.funcs:
				current = appliedfunc(current, probfunc())
			
			if not current in newprob.keys():
				newprob[current] = 0
			newprob[current] += 1.0
		
		self.probabilities = {}
		for value, probability in newprob.items():
			self.probabilities[value] = probability / numberOfSimulations
	
	def apply_probability(self, probabilityFunction, appliedFunction):
		self.funcs.append((probabilityFunction, appliedFunction))
	
	def add(self, probabilityFunction):
		self.apply_probability(probabilityFunction, lambda x, y: x + y)
	
	def subtract(self, probabilityFunction):
		self.apply_probability(probabilityFunction, lambda x, y: x - y)
	
	def multiply(self, probabilityFunction):
		self.apply_probability(probabilityFunction, lambda x, y: x * y)
	
	def apply_function(self, function):
		self.funcs.append((lambda: 0, function))
	
	def add_constant(self, constant):
		self.apply_function(lambda x, y: x + constant)
	
	def subtract_constant(self, constant):
		self.apply_function(lambda x, y: x - constant)
		
	def multiply_constant(self, constant):
		self.apply_function(lambda x, y: x * constant)
	
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
