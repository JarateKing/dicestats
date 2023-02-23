from enum import Enum

class comparison(Enum):
    EQUAL = 1
    AT_LEAST = 2
    AT_MOST = 3
    LESS_THAN = 4
    MORE_THAN = 5

def print_output(probabilities, includeLabel, includePercent, includePlot, labelOverrides = {}, precision = 4, width = 100, barchar = '#', relativeBars = False, comparisonType = comparison.EQUAL):
    maxvaluewidth = 0
    maxpercent = 0
    
    if (includeLabel):
        for value in (labelOverrides.values() if labelOverrides else probabilities.keys()):
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
    
    if (includePlot):
        for value, probability in probabilities.items():
            maxpercent = max(maxpercent, probability * 100)
    
    if comparisonType != comparison.EQUAL:
        maxpercent = 100
            
    current = 0
    if (comparisonType == comparison.MORE_THAN) or (comparisonType == comparison.AT_LEAST):
        current = 1
        
    for value, probability in probabilities.items():
        output = ''
        
        if comparisonType == comparison.EQUAL:
            current = probability
        elif comparisonType == comparison.MORE_THAN:
            current -= probability
        elif comparisonType == comparison.AT_MOST:
            current += probability
        
        if (includeLabel):
            if labelOverrides:
                output += "{0:<{1}}: ".format(labelOverrides[value], maxvaluewidth)
            else:
                output += "{0: >{1}d}: ".format(value, maxvaluewidth)
        if (includePercent):
            output += "{0:{2}.{1}f}% ".format(current * 100, precision, precision + 4)
        if (includePlot):
            output += barchar * round(current * 100 / ((maxpercent if relativeBars else 100) / width))
        
        if comparisonType == comparison.LESS_THAN:
            current += probability
        elif comparisonType == comparison.AT_LEAST:
            current -= probability
        
        print(output)
        
    print()
