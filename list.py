#1.create a list and print unique elements in list
lst=[]
lst1=[]
n=int(input("enter total number"))
for i in range(n):
    lst.insert(i,int(input()))
print(lst)
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)
#2. print even numbers from list
lst=[]
lst1=[]
n=int(input("enter total number"))
for i in range(n):
    lst.insert(i,int(input()))
print(lst)
for i in lst:
    if(i%2==0):
        lst1.append(i)
print(lst1)
#3. create a list and print square of every item in new list.
lst=[]
lst1=[]
n=int(input("enter total number"))
for i in range(n):
    lst.insert(i,int(input()))
print(lst)
for i in lst:
    i=i**2
    lst1.append(i)
print(lst1)
#4. cocatenate two list
lst1=[]
lst2=[]
n=int(input("enter total number"))
for i in range(n):
    lst1.insert(i,int(input()))
for j in range(n):
    lst2.insert(j,int(input()))
print(lst1)
print(lst2)
lst1.extend(lst2)
print(lst1)
#5. create a list and find sum and average of elements in list
lst=[]
n=int(input("enter total number"))
for i in range(n):
    lst.insert(i,int(input()))
print(lst)
s=0
for i in lst:
    s=s+i
print("sum=",s)
avg=s//n
print("average=",avg)