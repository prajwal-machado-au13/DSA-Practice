def binSearch(arr,target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr=[1, 2, 7, 9, 11, 15, 45, 78, 90]
    idx=binSearch(arr,11)
    print(idx)