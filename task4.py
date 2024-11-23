from random import *

def create2DArray(x,y):
    array = []
    for i in range(0,y):
        array.append([])
        for j in range(0,x):
            array[i].append([])
            array[i][j] = '00'
    return array

def display2DArray(array):
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if len(str(array[i][j])) == 1:
                print(" ",end='')
            print(str(array[i][j]),end=' ')
        print('')

def fill_array_randint(x,y):
    array = create2DArray(x,y)
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            array[i][j] = int(randint(1,9))

    return array

def topTrig(array):
    out = []
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if i <= j:
                out.append(array[i][j])

    return out

def botTrig(array):
    out = []
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if i >= j:
                out.append(array[i][j])

    return  out

def sqrSum(list):
    out = 0
    for i in list:
        out += i*i

    return out

array1 = fill_array_randint(4,4)
display2DArray(array1)

print("")
print(f"bottom triangle: {sqrSum(botTrig(array1))}")
print(f"top triangle: {sqrSum(topTrig(array1))}")
