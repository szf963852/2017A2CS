# S3C3 Godfrey
# queue version 2

class Node():
    def __init__(self):
        self.Next=None
        self.content=None

def init():
    global Nullpointer,StartPointer, FreeListPointer,busy,List,RealPointer
    Nullpointer=-1
    StartPointer=Nullpointer
    FreeListPointer=0
    RealPointer=0
    List=[0]*10
    busy=0
    for i in range(10):
        List[i]=Node()
        List[i].Next=i+1
    List[9].Next=Nullpointer

def InsertNode(n):
    global Nullpointer, StartPointer, FreeListPointer,busy,List,RealPointer
    if busy==10:
        print("No extra space")
    elif StartPointer==Nullpointer:
        StartPointer = FreeListPointer
        s=FreeListPointer
        FreeListPointer = List[FreeListPointer].Next
        List[s].Next = Nullpointer
        List[s].content = n
        busy += 1
    else:
        k = RealPointer
        List[k].Next = FreeListPointer
        RealPointer=FreeListPointer
        List[FreeListPointer].content = n
        S = FreeListPointer
        FreeListPointer = List[FreeListPointer].Next
        List[S].Next = Nullpointer
        busy += 1

def SearchNode(n):
    global Nullpointer, StartPointer, FreeListPointer, busy, List
    k = StartPointer
    for i in range(busy-1):
        if n != List[k].content:
            k = List[k].Next
        if n == List[k].content:
            print("we find number",n,"in position",k)
            return k
            #     this returns the index of the item in the list, which begins from zero
    #     circular queue, so it shows the current position which is different to the value count from StartPointer
    print("no value found")
    return None

def PrintList():
    global Nullpointer, StartPointer, FreeListPointer, busy, List
    n = StartPointer
    for i in range(busy):
        print(List[n].content,end="   " )
        n = List[n].Next
    print("")

def DeleteNode():
    global Nullpointer, StartPointer, FreeListPointer, busy, List
    if busy!=0:
        List[StartPointer].content=None
        S = StartPointer
        F = FreeListPointer
        StartPointer = List[S].Next
        List[S].Next = FreeListPointer
        FreeListPointer=S
    busy=busy-1
#     treat it as a circular queue


# just test, not related to the function
init()
InsertNode(1)
PrintList()
InsertNode(3)
InsertNode(2)
InsertNode(5)
InsertNode(3)
InsertNode(6)
DeleteNode()
DeleteNode()
DeleteNode()
DeleteNode()
InsertNode(9)
InsertNode(5)
InsertNode(5)
InsertNode(3)
InsertNode(6)
PrintList()
# DeleteNode()
# DeleteNode()
# PrintList()
# DeleteNode()
# DeleteNode()
PrintList()
DeleteNode()
DeleteNode()
PrintList()
InsertNode(5)
PrintList()
# SearchNode(5)
InsertNode(9)
InsertNode(5)
# Del1eteNode()
DeleteNode()
DeleteNode()
DeleteNode()
# DeleteNode()
PrintList()
InsertNode(3)
PrintList()
InsertNode(6)
PrintList()
DeleteNode()
DeleteNode()
PrintList()
# InsertNode(5)
# PrintList()
