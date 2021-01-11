def mergeSort(arr1,arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    arr=[]
    i = 0
    j = 0

    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i = i + 1
        else:
            arr.append(arr2[j])
            j = j + 1
    while i < len1:
        arr.append(arr1[i])
        i = i + 1
    while j < len2:
        arr.append(arr2[j])
        j = j + 1
    return arr 



arr1 = [2,3,5,7]
arr2 = [1,4,6,9,11]
print(mergeSort(arr1,arr2))