# S3C3
# Godfrey coding bat

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
# print(factorial(5))

def bunnyEars(x):
    if x==0:
        return 0
    else:
        return 2+bunnyEars(x-1)
# print(bunnyEars(5))

def fibonacci(x):
    if x==0:
        return 0
    if x==1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)
# print(fibonacci(6))

def bunnyEars2(x):
    if x==0:
        return 0
    if x%2==1:
        return 2+bunnyEars2(x-1)
    else:
        return 3+bunnyEars2(x-1)
# print(bunnyEars2(5))

def  triangle(x):
    if x==0:
        return 0
    else:
        return x+triangle(x-1)
# print(triangle(3))

def sumDigits(x):
    if x==0:
        return 0
    else:
        return x%10+sumDigits(x//10)
# print(sumDigits(169))

def count7(x):
    if x==0:
        return 0
    if x%10==7:
        return 1+count7(x//10)
    return count7(x//10)
# print(count7(727))

def count8(x):
    if x==0:
        return 0
    if x%10==8 :
        if (x//10)%10==8:
            return 2+count8(x//10)
        return 1 + count8(x // 10)
    return count8(x//10)
# print(count8(81888))

def powerN(base,n):
    if n==0:
        return 1
    else:
        return base*powerN(base,n-1)
# print(powerN(4,5))

def countX(n):
    if n=="":
        return 0
    elif n[len(n)-1]=="x":
        return 1+countX(n[0:len(n)-1])
    else:
        return countX(n[0:len(n)-1])
# print(countX("dsaxx"))

def countHi(n):
    if n=="":
        return 0
    elif n[-2:]=="hi":
        return 1+countHi(n[0:len(n)-1])
    else:
        return countHi(n[0:len(n)-1])
# print(countHi("hih"))

def changeXY(n):
    if n=="":
        return ""
    elif n[len(n)-1]=="x":
        return changeXY(n[0:len(n)-1])+"y"
    else:
        return changeXY(n[0:len(n)-1])+n[len(n)-1]
# print(changeXY("ssx"))

def changePi(n):
    if n=="":
        return ""
    elif n[-2:]=="pi":
        return changePi(n[0:len(n)-2])+"3.14"
    else:
        return changePi(n[0:len(n)-1])+n[len(n)-1]
# print(changePi("pip"))

def noX(n):
    if n=="":
        return ""
    elif n[len(n)-1]=="x":
        return noX(n[0:len(n)-1])+""
    else:
        return noX(n[0:len(n)-1])+n[len(n)-1]
# print(noX("ssxxxxx"))

def array6(list, index):
    if index>=len(list):
        return False
    else:
        if list[index]==6:
            return True
        else:
            return array6(list,index+1)
# print(array6([0,1,8],0))

def array11(list,index):
    if index>=len(list):
        return 0
    else:
        if list[index]==11:
            return 1+array11(list,index+1)
        else:
            return array11(list,index+1)
# print(array11([0,11,2],0))

def array220(list, index):
    if index>=len(list)-1:
        return False
    else:
        if list[index]==list[index+1]/10:
            return True
        else:
            return array220(list,index+1)
# print(array220([0,2,20],0))

def allstar(n):
    if len(n)==1:
        return n
    else:
        return allstar(n[0:len(n)-1])+"*"+n[-1:]
# print(allstar("hello"))

def pairstar(n):
    if len(n)==1:
        return n
    else:
        if n[len(n)-1]==n[len(n)-2]:
            return pairstar(n[0:len(n)-1])+"*"+n[-1:]
        return pairstar(n[0:len(n)-1])+n[-1:]
# print(pairstar("aaaa"))

def endX(n):
    if n=="":
        return ""
    else:
        if n[0]=="x":
            return endX(n[1:len(n)])+"x"
        return n[0]+endX(n[1:len(n)])
# print(endX("xhixhix"))

def countPairs(n):
    if len(n)==2:
        return 0
    else:
        if n[-1]==n[-3]:
            return countPairs(n[0:len(n)-1])+1
        return countPairs(n[0:len(n)-1])
# print(countPairs("axaxa"))

def countAbc(n):
    if len(n)==2:
        return 0
    else:
        if n[-3:]=="abc"or n[-3:]=="aba":
            return countPairs(n[0:len(n)-1])+1
        return countPairs(n[0:len(n)-1])
# print(countAbc("abaxxabc"))

def count11(n):
    if len(n)==1 or len(n)==0:
        return 0
    else:
        if n[-2:]=="11":
            return count11(n[0:len(n)-2])+1
        return count11(n[0:len(n)-1])
# print(count11("1111"))

def stringClean(n):
    if len(n)==1:
        return n
    else:
        if n[0]==n[1]:
            return stringClean(n[1:len(n)])
        else:
            return n[0]+stringClean(n[1:len(n)])
# print(stringClean("abbbcdd"))

def countHi2(n):
    if len(n)<=1:
        return 0
    elif n[:2] == "hi":
        return 1 + countHi2(n[2:len(n)])
    elif n[:3] == "xhi":
        return countHi2(n[3:len(n)])
    else:
        return countHi2(n[1:len(n)])
# print(countHi2("xhiahi"))

def parenBit(n):
    if n[0]=="("and n[-1]==")":
        return n
    else:
        if n[0]!="(":
            return parenBit(n[1:])
        if n[-1]!=")":
            return parenBit(n[:-1])
# print(parenBit("x(hello)sda"))

def nestparen(n):
    if n[0] != "(" :
        if n[0]!=")":
            return False
        else:
            return True
    else:
        return nestparen(n[1:])
# print(nestparen("(((()))"))

def strcount(n,s):
    if len(n)<=len(s)-1:
        return 0
    else:
        if n[-len(s):]==s:
            return strcount(n[0:len(n)-len(s)],s)+1
        return strcount(n[0:len(n)-1],s)
# print(strcount("catcowcat", "cat"))

def strCopies(n,s,k):
    if k==0:
        return True
    if len(n)<=len(s)-1:
        return False
    else:
        if n[-len(s):]==s:
            return strCopies(n[0:len(n)-len(s)],s,k-1)
        return strCopies(n[0:len(n)-1],s,k)
# print(strCopies("catcowcat", "cat",2))

def strDist(n,s):
    if n[0:len(s)]==s and n[-len(s):]==s:
        return len(n)
    else:
        if n[0:len(s)]==s:
            return strDist(n[1:],s)
        if n[:-len(s)]==s:
            return strDist(n[:-1],s)
# print(strDist("catcwcat", "cat"))

