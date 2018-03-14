# chapter 27 end of chapter
## S3C3 Godfrey
#### 1 a 
                    BankAccount
                     /     \
        personaccount      Saving account
##### b
```python
class BankAccount :
    def __init__(self, i): 
        self.HolderName = ''
        self.IBAN = i
        
    def SetAccountHolderName(self, n):
        self.HolderName = n
        
    def GetAccountHolderName(self):
        return(self.HolderName)
        
    def GetIBAN(self):
        return(self.IBAN)
```
##### c i
personalAccount should have attributes MonthlyFee, OverDraftLimit
##### c ii
SavingAccount should have attributes interestrate
##### 2 a
SeasonTicketHolder:
    EmailAddress : string
    GetHolderName()
    GetEmailAddress()
    
Pav-As-You-Go-TicketHolder: 
    Amount : CURRENCY
    Constructor(Name: STRING, email : STRING)
    GetAmount()
    UpdateAmount()

ContractTi cketHolder:
    MonthlyFee : CURRENCY
    GetFee()
    
###### bi 
private attributes are declared which can not be used or changed by program outside the class

###### bii 
public attribute can be accessed directly

##### c
```python
Customer = ContractTicketHolder("A. Smith","xyz@abc.xx", 10)
```

##### 3a
containment

##### 3 b
```python
class NodeClass :
    def __init__(self):
        self.Data = ''
        self.Pointer = -1
        
    def SetData(self, d):
        self.Data = d
        
    def GetData(self):
        return(self.Data)
        
    def SetPointer(self, x):
        self.Data = x
        
    def GetPointer(self):
        return(self.Pointer)
```

##### 3 c
```python
class QueueClass :
    def __init__(self):
        self.Queue = [NodeClass() for i in range(51)]
        self.Head = -1
        self.Tail = -1
```

##### 3 d
```python
def JoinQueue(self, d):
    if Head == -1 :
    Head = 0
    self.Tail += 1
    i = self.Tail
    self.Queue[i].SetData(d)

```



