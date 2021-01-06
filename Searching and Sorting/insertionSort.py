def insertionSort(li):
    for idx in range(1,len(li)):
        pos=idx
        curr=li[idx]
        while pos>0 and li[pos-1]>curr:
            li[pos]=li[pos-1]
            pos=pos-1
        li[pos]=curr
    return li


input=[1,7,2,3,4,8,9]
output=insertionSort(input)
print(*output)
