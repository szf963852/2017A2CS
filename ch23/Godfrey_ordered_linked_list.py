#S3C3 Godfrey
# ordered list


class Node():
    def __init__(self):
        self.Next=None
        self.content=None

def init():
    global Nullpointer,StartPointer, FreeListPointer,busy,List
    Nullpointer=-1
    StartPointer=Nullpointer
    FreeListPointer=0
    List=[0]*10
    busy=0
    for i in range(10):
        List[i]=Node()
        List[i].Next=i+1
    List[9].Next=Nullpointer

def InsertNode(n):
    global Nullpointer, StartPointer, FreeListPointer,busy,List
    if busy==10:
        print("No extra space")
    elif StartPointer==Nullpointer:
        StartPointer=FreeListPointer
        s=FreeListPointer
        FreeListPointer = List[FreeListPointer].Next
        List[s].Next=Nullpointer
        List[s].content = n
        busy += 1
    else:
        if  List[StartPointer].content>=n:
            s=FreeListPointer
            FreeListPointer = List[FreeListPointer].Next
            List[s].content=n
            List[s].Next=StartPointer
            StartPointer=s
        else:
            k=StartPointer
            l=True
            for i in range(busy-1):
                if List[k].content<n:
                    m=k
                    k=List[k].Next
                if List[k].content>n:
                    l=False
            if l==True:
                List[k].Next=FreeListPointer
                List[FreeListPointer].content = n
                S=FreeListPointer
                FreeListPointer = List[FreeListPointer].Next
                List[S].Next = Nullpointer
            if l==False:
                List[m].Next = FreeListPointer
                List[FreeListPointer].content = n
                S = FreeListPointer
                FreeListPointer = List[FreeListPointer].Next
                List[S].Next = k
        busy+= 1


def SearchNode(n):
    global Nullpointer, StartPointer, FreeListPointer, busy, List
    k = StartPointer
    if busy==1 and n==List[StartPointer].content:
        return StartPointer
    for i in range(busy-1):
        if n>List[k].content:
            k = List[k].Next
        if n == List[k].content:
            return k
    print("no value found")

def PrintList():
    global Nullpointer, StartPointer, FreeListPointer, busy, List
    n = StartPointer;
    if busy==0:
        print("nothing")
    else:
        for i in range(busy):
            print(List[n].content,end="   " )
            n = List[n].Next
        print("")

def DeleteNode(n):
    global Nullpointer, StartPointer, FreeListPointer, busy, List
    if SearchNode(n)!=None:
        if n==List[StartPointer].content:
            List[StartPointer].content=None
            k=FreeListPointer
            while List[k].Next != Nullpointer:
                k = List[k].Next
            List[k].Next=StartPointer
            a=StartPointer
            StartPointer = List[StartPointer].Next
            List[a].Next=Nullpointer
        else:
            k=StartPointer
            while n!=List[k].content:
                m = k
                k = List[k].Next
            List[m].Next=List[k].Next
            i=FreeListPointer
            while List[i].Next!=Nullpointer:
                i= List[i].Next
            List[i].Next = k
            List[k].Next = Nullpointer
        busy-=1

init()
InsertNode(1)
PrintList()
InsertNode(3)
InsertNode(1)
PrintList()
InsertNode(6)
PrintList()
DeleteNode(1)
DeleteNode(1)
DeleteNode(3)
# DeleteNode(6)
InsertNode(5)
PrintList()
# InsertNode(5)
# PrintList()
# DeleteNode(5)
# PrintList()
# InsertNode(1)
# PrintList()
# DeleteNode(1)
# PrintList()
# SearchNode(6)
# DeleteNode(2)
# DeleteNode(3)
# PrintList()
# DeleteNode(6)
# PrintList()
# InsertNode(2)
# InsertNode(1)
# PrintList()
# InsertNode(3)
# PrintList()



