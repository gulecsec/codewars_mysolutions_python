def find_slope(points):
    y = points[3] - points[1]
    x = points[2] - points[0]
    if x == 0 and y == 0:
        return "undefined"
    elif y == 0:
        return str(y)
    elif x == 0:
        return "undefined"
    
    else:
        return str(int(y/x))