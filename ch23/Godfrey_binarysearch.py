def binarySearch(arr,value):
    low=0
    high=len(arr)
    mid=len(arr)//2
    while arr[mid]!=value:
        if value>arr[mid]:
            low=mid
            mid=low+(high-low)//2
        else:
            high=mid
            mid=low+(high-low)//2
    return mid+1

print("test:",binarySearch([1,3,6,8,11,15,18,19,21,25,27,29,35,36,39,40,45,47,49],25))
