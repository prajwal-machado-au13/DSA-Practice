def insertionSort(li):
    for idx in range(1,len(li)):
        pos = idx - 1
        key = li[idx]
        while pos>=0 and key < li[pos]:
            li[pos+1]=li[pos]
            pos=pos-1
        li[pos+1] = key
    return li


input=[1,7,2,3,4,8,9]
output=insertionSort(input)
print(*output)
