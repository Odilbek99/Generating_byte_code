# average of elements in list

def point():
    list_ = [1,2,3,3,4,6,6,5,54,45,65,65,65,65,5645]
    c = 0
    for i in list_:
        c = c+i
    average = c/len(list_)
    print(f'Average is:  ', average)