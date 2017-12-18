# S3C3 Godfrey
# stack

class Node():
    def __init__(self):
        self.Next=None
        self.content=None

def init():
    global Nullpointer,BaseofstackPointer, FreeListPointer,busy,List
    Nullpointer=-1
    BaseofstackPointer=Nullpointer
    FreeListPointer=0
    List=[0]*10
    busy=0
    for i in range(10):
        List[i]=Node()
        List[i].Next=i+1
    List[9].Next=Nullpointer

def InsertNode(n):
    global Nullpointer, BaseofstackPointer, FreeListPointer,busy,List
    if busy==10:
        print("No extra space")
    # elif BaseofstackPointer==Nullpointer:
    elif busy==0:
        BaseofstackPointer = 0
        List[0].Next = Nullpointer
        List[FreeListPointer].content = n
        FreeListPointer = 1
        busy += 1
    else:
        k=BaseofstackPointer
        while List[k].Next!=Nullpointer:
            k = List[k].Next
        List[k].Next=FreeListPointer
        List[FreeListPointer].content=n
        S = FreeListPointer
        FreeListPointer = List[FreeListPointer].Next
        List[S].Next = Nullpointer
        busy+=1

def SearchNode(n):
    global Nullpointer, BaseofstackPointer, FreeListPointer, busy, List
    k = BaseofstackPointer
    for i in range(busy-1):
        if n != List[k].content:
            k = List[k].Next
        if n == List[k].content:
            return k
    #     this returns the index of the item in the list, which begins from zero
    print("no value found")

def PrintList():
    global Nullpointer, BaseofstackPointer, FreeListPointer, busy, List
    n = BaseofstackPointer
    for i in range(busy):
        print(List[n].content,end="   " )
        n = List[n].Next
    print("")

def DeleteNode():
    global Nullpointer, BaseofstackPointer, FreeListPointer, busy, List
    if busy!=0:
        if busy==1:
            List[BaseofstackPointer].content=None
            s=BaseofstackPointer
            BaseofstackPointer=Nullpointer
            List[BaseofstackPointer].Next=FreeListPointer
            FreeListPointer=s

        else:
            k=BaseofstackPointer
            while List[k].Next != Nullpointer:
                m=k
                k = List[k].Next
            List[m].Next = Nullpointer
            List[k].Next =FreeListPointer
            FreeListPointer=k
            List[k].content = None
        busy=busy-1

# just test, not related to the function
init()
InsertNode(1)
InsertNode(3)
InsertNode(2)
InsertNode(5)
InsertNode(3)
InsertNode(6)
DeleteNode()
DeleteNode()
DeleteNode()
InsertNode(9)
InsertNode(5)
PrintList()
InsertNode(3)
PrintList()
DeleteNode()
DeleteNode()
InsertNode(6)
PrintList()
InsertNode(5)
PrintList()
DeleteNode()
DeleteNode()
DeleteNode()
DeleteNode()
DeleteNode()
DeleteNode()
PrintList()
InsertNode(5)
PrintList()
InsertNode(7)
InsertNode(1)
PrintList()

