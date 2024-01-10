import math

def check_pnr(pnr):

    if type(pnr) != list or len(pnr) != 10: # Checks correct input
        return False
    
    for i in pnr:                           # For each number in the list
        if type(i) != int:                  # Asserts that its a correct value    
            return False        
    
    nylista = new_list(pnr)
    sumlista = sum_list(nylista)
    narmast = nearest(sumlista)
    kontroll = control(narmast, sumlista)
    
    return pnr[9] == kontroll
    
def nearest(x):
    return math.ceil(x / 10.0) * 10


def control(num1, num2):
    controlunit = abs (num2 - num1)
    return controlunit


def sum_list(nulista):
    
    sum = 0
    for i in range(len(nulista)):
        if nulista[i] >= 10:
            sum += nulista[i] // 10 + nulista[i] % 10
        else:
            sum += nulista[i]
    return sum


def new_list(pnr):

    vikt = [2,1,2,1,2,1,2,1,2,1]
    newlist = []
    
    for i in range(len(pnr[:9])):
        prod = pnr[i] * vikt[i]
        newlist.append(prod)
    return newlist

pnr = [9, 5, 0, 9, 0, 8, 5, 5, 5, 2]
is_true = check_pnr(pnr)
print(is_true)