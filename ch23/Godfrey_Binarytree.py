class treemode():
    def __init__(self):
        self.data = None
        self.Leftpointer = None
        self.Rightpointer = None


def init():
    global Nullpointer, RootPointer, FreePointer, Tree, Startpointer
    Startpointer=0
    Nullpointer =None
    RootPointer = Nullpointer
    FreePointer=0
    Tree = [0] * 10
    for i in range(10):
        Tree[i] = treemode()
        Tree[i].Leftpointer= i + 1
    Tree[9].Leftpointer=Nullpointer

def Insertnode(n):
    global Nullpointer, RootPointer, FreePointer, Tree, Startpointer
    if FreePointer!=Nullpointer:
        s=FreePointer
        Tree[s].data=n
        FreePointer = Tree[FreePointer].Leftpointer
        Tree[s].Leftpointer=Nullpointer
        Tree[s].Rightpointer=Nullpointer
        k=Startpointer
        if RootPointer==Nullpointer:
            RootPointer=s
        else:
            while (Tree[k].data>n and Tree[k].Leftpointer!=Nullpointer) or (Tree[k].data<n and Tree[k].Rightpointer!=Nullpointer):
                if Tree[k].data>n and Tree[k].Leftpointer!=Nullpointer:
                        k=Tree[k].Leftpointer
                elif Tree[k].data<n and Tree[k].Rightpointer!=Nullpointer:
                        k=Tree[k].Rightpointer
            if Tree[k].data>n:
                Tree[k].Leftpointer=s
            elif Tree[k].data<n:
                Tree[k].Rightpointer=s
            else:
                print("no equal numbers")
                FreePointer=s
                Tree[s].data = None
                Tree[s].Leftpointer = s+1

def Findnode(n):
    global Nullpointer, RootPointer, FreePointer, Tree, Startpointer
    k=RootPointer
    while k!=Nullpointer and n!=Tree[k].data:
        if n<Tree[k].data:
            k = Tree[k].Leftpointer
        else:
            k=Tree[k].Rightpointer
    return k




init()
Insertnode(5)
Insertnode(5)
Insertnode(5)
# print (Startpointer,FreePointer)
Insertnode(3)
# print (Startpointer,FreePointer)
Insertnode(3)
Insertnode(1)
Insertnode(2)
Insertnode(7)
# for i in range(10):
    # print(Tree[i].data,Tree[i].Leftpointer,Tree[i].Rightpointer)
# print(Findnode())