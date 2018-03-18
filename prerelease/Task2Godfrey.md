# task 2 of prerelease

#### 2.1
TOY:
|Attributes        | Functions|
|-|-|
|toy|constructor()|
|Name              | getname( )/setname( )|
|ID                    | getID( )/setID( )|
|Price               | getPrice( )/setPrice( )|
|Minimum age  | getMinimumage( )/setMinimumage( )|

ComputerGame:
Attributes        | Functions
|-|-|
|computer game|constructor()|
Category         | getcategory( )/setcategory( )
Console          | getconsole( )/setconsole( )

Vehicle
Attributes        | Functions
|-|-|
|vehicle|constructor()|
Type                | gettype( )/settype( )
Height             | getheight( )/setheight( )
Length             | getlength( )/setlength( )
Weight             | getweight( )/setweight( )

#### 2.2
inheritence means that one class's parameters is directly passed down to its subclasses

In the last example, computergame and vehicle are the subclasses of toy.

#### 2.3
```python
    class toy:
        def __init__(self,n,i,p,m):
            self.name=n
            self.id=i
            self.price=p
            self.minimumage=m
        
        def getname(self):
            return self.name
            
        def setname(self,name):
            self.name=name
            
        def getid(self):
            return self.id
        
        def setid(self,id):
            self.id=id
        
        def getprice(self):
            return self.price
            
        def setprice(self):
            self.price=price
        
        def getminimumage(self):
            return self.minimumage
       
       def setminimumage(self,min):
            self.minimumage=mim
```
        
#### 2.4
```python 
    class vehicle(toy):
        def__init__(self,n,i,p,m,t,h,l,w):
            toy.__init__(self,n,i,p,m)
            self.type=t
            self.height=h
            self.weight=w
            self.length=l
```    
            
#### 2.5
```python
    try:
        if age>0 and age<18:
            self.age=age
        else:
            age=input('please input again')
```

#### 2.6
```python
    vehicle=[ ]
    computergame=[ ]
    vehicle.append('Red Sports Car','RSC13',15.00,6,'car',3.3,12.1,0.08)
```

#### 2.7
```python
    def printdetails(id):
       i=0
       while toy[i].id!=id:
            i+=1
       Toy[i].printdetails()
```
        
#### 2.8
``` python
    def discount(n):
        n=n/100
        for i in range(len(toy)):
            toy[i].price=toy[i].price*n
```

#### 2.9

 a bubble sort compares the neighbor's values and change their position if their values don't fulfill the requirement.
 a insertion sort always try to find a appropriate place of insertion.
 
 ### 2.10
 
 ```python
    def sort():
        for i in range(len(toys)):
            itemtobeinserted=toy[i]
            c=i-1
            while itemtobeinserted.price<toy[c].price and c>0:
                toy[c+1]=toy[c]
                c-=1
            toy[c+1]=itemtobeinserted
```







