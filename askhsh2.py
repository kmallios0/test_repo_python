#askhsh 2
import random

def fibonacci(n):
    a = 0
    b = 1

    if n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return b
flag=False
while not flag:
    n=input("Δώσε n-οστό όρο")
    n=int(n)
    if n>=0:
        flag=True
    else:
        print("Δώσε άλλο αριθμό")



p=(fibonacci(n))
if p==1:
    print ("ο p είναι πρώτος και p=1")
else:
    i=0
    prime=True
    while i<20 and prime==True:
        a=random.randint(1,p)
        if a**p%p==a%p:
            i=i+1
        else:
            prime=False

    if prime==True:
        print("Ο" ,n,"ος αριθμός της ακολουθίας Fibonacci", p , "είναι πρώτος αριθμός")
    else:
        print("Ο" ,n,"ος αριθμός της ακολουθίας Fibonacci", p , "είναι πρώτος αριθμός")
