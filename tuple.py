'''#1. create a list of tuple
lst1=[]
lst2=[]
n=int(input("enter total number"))
for i in range(n):
    lst1.insert(i,int(input()))
for j in range(n):
    lst2.insert(j,int(input()))
lst=list(zip(lst1,lst2))
print(lst)
#2. append new elements in tuple.
tpl=()
n=int(input("enter total elements"))
for i in range(n):
    y=int(input())
    tpl=tpl+(y,)
print(tpl)
lst=list(tpl)
lst.extend((10,20,30))
tpl=tuple(lst)
print(tpl)
#3. replace an item of tuple in list.
lst1=[]
lst2=[]
lst3=[]
nlst=[]
n=int(input("enter total number in each list"))
for i in range(n):
    lst1.insert(i,int(input()))
for i in range(n):
    lst2.insert(i,int(input()))
for i in range(n):
    lst3.insert(i,int(input()))
lst=zip(lst1,lst2,lst3)
lst=list(lst)
for k in lst:
    m=(k[0],k[1])+(100,)
    print(m)
    nlst.append(m)
print(nlst)
#4. craete a tuple of unique elements.
tpl=()
tpl1=()
n=int(input("enter total number"))
for i in range(n):
    y=int(input())
    tpl+=y,
print(tpl)
for i in tpl:
    if i not in tpl1:
        tpl1+=i,
print(tpl1)'''
lst1=[]
lst2=[]
lst3=[]
n=int(input("enter total number in each list"))
for i in range(n):
    lst1.insert(i,int(input()))
for i in range(n):
    lst2.insert(i,int(input()))
lst=zip(lst1,lst2)
lst=list(lst)
print(lst)
for k in lst:
    m=k[0]
    p=k[-1]
lst3.extend((m,p))
print(lst3)