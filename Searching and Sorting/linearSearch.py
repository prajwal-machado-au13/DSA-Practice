def linSearch(li,target):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr=[1, 2, 7, 9, 5, 11, 15, 91, 6, 45, 78, 90]
    print(linSearch(arr,6))