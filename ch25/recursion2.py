def groupSum(start,list,target):
    if target ==0:
        return True
    if start==len(list):
        return False
    return groupSum(start+1,list,target-list[start]) or groupSum(start+1,list,target)
# print(groupSum(0,[2,4,6],10))

def groupSum6(start,list,target):
    if target == 6 and 6 in list:
        return True
    if start==len(list):
        return False
    if list[start]==6:
        return groupSum6(start+1,list,target)
    return groupSum6(start+1,list,target-list[start]) or groupSum6(start+1,list,target)
# print(groupSum6(0,[2,4,6],4))

def groupNoAdj(start,list,target):
    if target == 0:
        return True
    if start>=len(list):
        return False
    return groupNoAdj(start+2,list,target-list[start]) or groupNoAdj(start+1,list,target)
# print(groupNoAdj(0, [2, 5, 10, 4], 9))

def groupSum5(start,list,target):
    if target ==0:
        return True
    if start==len(list):
        return False
    if list[start]%5==0:
        if start!=len(list)-1:
            if list[start+1]==1:
                return   groupSum5(start + 2, list, target - list[start])
        return groupSum5(start+1,list,target-list[start])
    return groupSum5(start+1,list,target-list[start]) or groupSum5(start+1,list,target)
# print(groupSum5(0, [2, 5, 10,1, 4], 18))

def groupSumClump(start,list,target):
    if target == 0:
        return True
    if start == len(list):
        return False
    k=start
    if k<=len(list)-2:
        while list[k]==list[k+1] and k<=len(list)-2:
            k+=1
    s=k-start
    return groupSumClump(start + 1+ s , list, target - list[start]*(s+1)) or groupSum(start + 1 + s , list, target)
# print(groupSumClump(0, [2, 4, 4, 8], 14))

def helperSplitArray(start, nums, sum1, sum2):
    if start >= len(nums):
        if sum1==sum2:
            return True
        else:
            return False
    return helperSplitArray(start+1, nums, sum1+nums[start], sum2)  or helperSplitArray(start+1, nums, sum1, sum2+nums[start])

def splitArray(nums):
    if helperSplitArray(0, nums, 0, 0) == True:
        return True
    else:
        return False
# print(splitArray([2,4,2,16]))


def helperSplitOdd10(start, nums, sum1, sum2):
    if start >= len(nums):
        if (sum1%10==0 and sum2%2==1) or (sum2%10==0 and sum1%2==1):
            return True
        else:
            return False
    return helperSplitOdd10(start+1, nums, sum1+nums[start], sum2)  or helperSplitOdd10(start+1, nums, sum1, sum2+nums[start])

def splitOdd10(nums):
    if helperSplitOdd10(0, nums, 0, 0) == True:
        return True
    else:
        return False
# print(splitOdd10([5,5,1,8]))

def helperSplit53(start, nums, sum1, sum2):
    if start >= len(nums):
        if sum1==sum2:
            return True
        else:
            return False
    if nums[start]%5==0:
        return helperSplit53(start + 1, nums, sum1 + nums[start], sum2)
    if nums[start]%3==0:
        return helperSplit53(start+1, nums, sum1, sum2+nums[start])
    return helperSplit53(start+1, nums, sum1+nums[start], sum2)  or helperSplit53(start+1, nums, sum1, sum2+nums[start])

def split53(nums):
    if helperSplit53(0, nums, 0, 0) == True:
        return True
    else:
        return False
# print(split53([5,3,5,3]))


