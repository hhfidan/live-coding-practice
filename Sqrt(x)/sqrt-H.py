def sqrt(x):

    if x == 0:
        return 0

    y = x

    while y*y >x:

        y = (y+x/y)/2  #Newton-Raphson

    return int(y)
