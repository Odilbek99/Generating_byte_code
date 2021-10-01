import math

def factorial():
    list_ = [5,6,7]
    l = []
    for element in list_:
        l.append(math.factorial(element))
    print('Factorials:  ',l)

