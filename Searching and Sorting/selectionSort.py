def selectionSort(arr):
    for i in range(len(arr)-1):
        minIdx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIdx]:
                minIdx=j
        arr[i],arr[minIdx]=arr[minIdx],arr[i]
    return arr



li=[10,12,15,18,17,12,13]
res=selectionSort(li)
print(*res)