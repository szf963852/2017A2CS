class dicnode():
    def __init__(self,k=None,d=None):
        # in order to print it naturally,we give them the value None at first
        self.data = d
        self.key = k

Max=19
Hashtable = [dicnode()] * (Max+1)

def charToNum(c):
    if c.isalpha():
        return ord(c)
    else:
        return

def Insert(key,data):
    index=charToNum(key[0])
    index=index%(Max+1)
    while Hashtable[index].key!=None and Hashtable[index].key!=key:
        index=index+1
        if index>Max:
            index=0
    Hashtable[index]=dicnode(key,data)

def FindRecord(k):
    index = charToNum(k[0])
    Index=index%(Max+1)
    while (Hashtable[Index].key!=k) and (Hashtable[Index].key!=None):
        Index+=1
        if Index>Max:
            Index=0
    if Hashtable[Index].key!=None:
        print("the definition of", Hashtable[Index].key,"is",Hashtable[Index].data)
        return Hashtable[Index].data
    return None

def printdic():
    # if you want, you can see the content of the whole table
    for i in range((Max+1)):
        print(Hashtable[i].key,Hashtable[i].data)

Insert("PSTNs","public switched telephone networks")
Insert("ALU","arithmetic and logic unit")
Insert("ADCs","analogue-to-digital converters")
Insert("BCD","binary coded decimal")
Insert("IEEE","Institute of Electrical and Electronics Engineers")
Insert("I/0","input/output system")
Insert("I/0","input/output system")
Insert("IEEE","Institute of Electrical and Electronics Engineers")
FindRecord("BCD")
FindRecord("I/0")
FindRecord("ADCs")
# printdic() you can print all the table by this method