def print_output(probabilities, includeLabel, includePercent, includePlot, precision = 4, width = 100, barchar = '#', relativeBars = False):
    maxvaluewidth = 0
    maxpercent = 0
    
    if (includeLabel):
        for value in probabilities.keys():
            maxvaluewidth = max(maxvaluewidth, len(str(value)))
    
    if (includePlot):
        for value, probability in probabilities.items():
            maxpercent = max(maxpercent, probability * 100)
        
    for value, probability in probabilities.items():
        output = ''
        
        if (includeLabel):
            output += "{0: >{1}d}: ".format(value, maxvaluewidth)
        if (includePercent):
            output += "{0:{2}.{1}f}% ".format(probability * 100, precision, precision + 4)
        if (includePlot):
            output += barchar * round(probability * 100 / ((maxpercent if relativeBars else 100) / width))
        
        print(output)
        
    print()
