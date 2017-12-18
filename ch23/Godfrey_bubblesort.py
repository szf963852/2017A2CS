def bubble(a):
    for n in range(len(a)):
        k=0
        for n in range(len(a)-k-1):
            if a[n]>a[n+1]:
                b=a[n]
                a[n]=a[n+1]
                a[n+1]=b
    k+=1
    return a
