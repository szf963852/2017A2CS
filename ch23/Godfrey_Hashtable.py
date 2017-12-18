Hashtable = [None] * 10
Max=9


def Insert(n):
    index=n%10
    while Hashtable[index]!=None:
        index=index+1
        if index>Max:
            index=0
    Hashtable[index]=n

def FindRecord(n):
    Index=n%10
    while (Hashtable[Index]!=n) and (Hashtable[Index]!=None):
        Index+=1
        if Index>Max:
            Index=0
    if Hashtable[Index]!=None:
        return Index
    return None

def printhas():
    for i in range(10):
        print(Hashtable[i],end=" ")
    print("")

Insert(5)
Insert(25)
Insert(25)
Insert(6)
Insert(6)
Insert(6)
Insert(10)
printhas()
# print(FindRecord())

