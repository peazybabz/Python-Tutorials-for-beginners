def newLine (list):
    if (len(list)> 4):
        #Point A coordinates are the first 2 numbers of the sequence
        pointA = [float(list(1)), float(list(2))]
        pointB = [float(list(3)), float(list(4))]
        #line is defined with a tuple so the points cannot be modified
        line = (pointA, pointB);
        return line
    return'\nRuntime Error: Not enough arguements to create a line, 04 required'


