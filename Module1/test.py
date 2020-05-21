

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def linear_search(lst,key):
    for index,item in enumerate(lst):
        if item==key:
            return index
    return -1

