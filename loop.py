'''#1. print table of a given number.
n=int(input("enter number"))
i=1
while(i<=10):
    print("%d*%d=%d"%(n,i,i*n))
    i+=1
#2.program to check number is neon or not.
n=int(input("enter number"))
s=0
n1=n**2
while(n1>0):
    r=n1%10
    s=s+r
    n1=n1//10
if(s==n):
    print("it is neon number")
else:
    print("it is not neon number")
#3. count total number of digits in number.
n=int(input("enter any number"))
c=0
while(n>0):
    r=n%10
    c+=1
    n=n//10
print(c)'''
#4. program to find elements in list which are at odd index.
lst=[]
n=int(input("enter total number"))
for i in range(n):
    lst.insert(i,int(input()))
print(lst)
i=1
while(i<=len(lst)):
    if(i%2==1):
        print(lst[i])
    i=i+2
#5.print pattern(butterfly)
r=int(input())
sp=8
for i in range(1,r):
  print("*"*i+" "*sp+"*"*i,end='')
  print()
  sp=sp-2
sp=0
for i in range(r,0,-1):
  print("*"*i+" "*sp+"*"*i,end='')
  print()
  sp=sp+2