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

def shiftRow(row:list,n:int):
    if n%2 == 0:
        i = 0
        while True:
            noSwap = True
            for j in range(0, len(row) - 1):
                if row[j] < row[j + 1]:
                    row[j], row[j + 1] = row[j + 1], row[j]
                    noSwap = False
            i += 1
            if noSwap:
                break
    else:
        i = 0
        while True:
            noSwap = True
            for j in range(0, len(row) - 1):
                if row[j] > row[j + 1]:
                    row[j], row[j + 1] = row[j + 1], row[j]
                    noSwap = False
            i += 1
            if noSwap:
                break

def shiftRows(array:list):
    for i in range(0,len(array)):
        shiftRow(array[i],i)

array1 = fill_array_randint(5,7)

display2DArray(array1)


shiftRows(array1)

print("--------------------------------------")

display2DArray(array1)