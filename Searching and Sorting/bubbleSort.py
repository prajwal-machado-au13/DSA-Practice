def bubbleSort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array


li=[4,6,7,2,3,0]
result = bubbleSort(li)
print(*result)

