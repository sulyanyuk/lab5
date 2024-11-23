from random import *

# seed("12fgdgdgfgd3") ##################### global seed for testing


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

# Clarification: "Average without counting the outliers" is interpreted as the sum of all elements, minus the smallest
# and the largest, divided by n * m -2

# "Последовательность" is also interpreted in different ways, see comments below

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################


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

array1 = fill_array_randint(3,3)
array2 = fill_array_randint(3,3)
array3 = fill_array_randint(3,3)

display2DArray(array1)
print("--------------------------------------------")
display2DArray(array2)
print("--------------------------------------------")
display2DArray(array3)

def avgNoOut(array):
    maximum = array[0][0]
    minimum = array[0][0]
    elementSum = 0
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if array[i][j] < minimum:
                minimum = array[i][j]
            if array[i][j] > maximum:
                maximum = array[i][j]
            elementSum += array[i][j]
    avg = (elementSum - (minimum + maximum)) / (len(array)*len(array[0])-2)
    return avg

avg3M = [avgNoOut(array1),avgNoOut(array2),avgNoOut(array3)]

print(avg3M)

### if the task implies the numbers progressively get bigger/smaller (integer avg values don't show up often)

if avg3M[2] > avg3M[1] > avg3M[0]:
    print("Возрастают")
elif avg3M[2] < avg3M[1] < avg3M[0]:
    print("Убывают")
else:
    print("Нет посл ):")
    
# ### Require the numbers to be an equal distance from each other
# if abs(avg3M[0]- avg3M[1]) == abs(avg3M[1]- avg3M[2]):
#
#     if avg3M[2] > avg3M[1] > avg3M[0]:
#         print("Возрастают")
#     elif avg3M[2] < avg3M[1] < avg3M[0]:
#         print("Убывают")
#     else:
#         print("Нет посл ):")
#
# ### Require the numbers to be different by 1
#
# if (abs(avg3M[0] - avg3M[1]) == 1) and (abs(avg3M[1] - avg3M[2]) == 2):
#
#     if avg3M[2] > avg3M[1] > avg3M[0]:
#         print("Возрастают")
#     elif avg3M[2] < avg3M[1] < avg3M[0]:
#         print("Убывают")
#     else:
#         print("Нет посл ):")