# task 2 of prerelease

#### 2.1
TOY:
|Attributes        | Functions|
|-|-|
|toy|constructor()|
|Name(string) | getname( )/setname( )|
|ID(string)             | getID( )/setID( )|
|Price(real)              | getPrice( )/setPrice( )|
|Minimum age(integer) | getMinimumage( )/setMinimumage( )|

ComputerGame:
Attributes        | Functions
|-|-|
|computer game|constructor()|
Category(string)         | getcategory( )/setcategory( )
Console(string)       | getconsole( )/setconsole( )

Vehicle
Attributes        | Functions
|-|-|
|vehicle|constructor()|
Type (string)             | gettype( )/settype( )
Height (integer)           | getheight( )/setheight( )
Length (interger)            | getlength( )/setlength( )
Weight  (weight)           | getweight( )/setweight( )

#### 2.2
inheritence means that one class's parameters is directly passed down to its subclasses

In the last example, computergame and vehicle are the subclasses of toy.

#### 2.3
```python
    class toy:
        def __init__(self,n,i,p,m):
            self._name=n
            self._id=i
            self._price=p
            self._minimumage=m
        
        def getname(self):
            return self._name
            
        def setname(self,name):
            self._name=name
            
        def getid(self):
            return self._id
        
        def setid(self,id):
            self._id=id
        
        def getprice(self):
            return self._price
            
        def setprice(self):
            self._price=price
        
        def getminimumage(self):
            return self._minimumage
       
       def setminimumage(self,min):
            self._minimumage=mim
```
        
#### 2.4
```python
    class computergame(toy):
	def__init__(self,n,i,p,m,c,o):
            toy.__init__(self,n,i,p,m)
            self._category=c
            self._console=o
            
	def getcategory(self):
	    return self._category
	
	def setcategory(self,c):
	    self._catrgory=c
	
	def getconsole(self):
	    return self._console
	
	def setconsole(self,o):
	    self._console=o
	

    class vehicle(toy):
        def__init__(self,n,i,p,m,t,h,l,w):
            toy.__init__(self,n,i,p,m)
            self.type=t
            self._height=h
            self._weight=w
            self._length=l

	def gettype(self):
	    return self._type
	
	def setcontype(self,o):
	    self._type=o

	def getlength(self):
	    return self._length
	
	def setlength(self,o):
	    self._length=o
   
```    
            
#### 2.5
```python
    try:
        if age>0 and age<18:
            self.__age=age
        else:
            age=input('please input again')

    class toy:
	def __init__(self,n,i,p,m):
	    toy.setname(self,n)
	    toy.setid(self,i)
	    toy.setprice(self, p)
	    toy.setminage(self,m)
	    
```

#### 2.6
```python
    vehicle=[ ]
    computergame=[ ]
    vehicle.append('Red Sports Car','RSC13',15.00,6,'car',3.3,12.1,0.08)
    vehicle.append('14d','L4D01',10,15,'FPS','PC')
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







