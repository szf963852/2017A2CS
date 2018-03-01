```python
## a(i)
	class CustomerRecord :  
    def \_\_init\_\_(self) :  
        self.CustomerID = 0  
  self.CustomerName = ""  
  self.TelNumber = 0  
  self.TotalOrders = ""  
## a(ii)
CustomerData = \[CustomerRecord() for i in range(10)\]  

## b(i)  
def Hash(ID) :  
    return(ID % 1000)  
## b(ii)
def AddRecord(CustomerData, Customer):  
    address = Hash(Customer.CustomerID)  
    while CustomerData(address).CustomerID != 0 :  
        address += 1  
  if address == 1000 :  
            address = 0  
  CustomerData\[address\] = Customer  

## b(iii) 
def FindRecord(CustomerData, ID):  
    address = Hash(ID)  
    while CustomerData\[address\].CustomerID != ID :  
        address += 1  
  if address == 1000:  
            address = 0  
  return (address)  
  
 ##c
import pickle  
  
def SaveData(CustomerData) :  
    CustomerFile = open('CustomerData.Dat','wb')  
    for i in range(1000) :  
        pickle.dump(CustomerData\[i\], CustomerFile)  
    CustomerFile.close()
```
##### first we should set up fixed length records and save them to a random file by hash table. Then, add Record needs to update the correct record in the random file.  then use the hash table again during find function to access it directly.




```python 
def OpenFile() :  
    FileName = input("Which file you want? ")  
    try:  
        Channel = open(FileName, 'rb+')  
    except :  
        print("File does not exist")
 ```