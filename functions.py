'''#1.find factorial of number using function
def fact(n):
    f=1
    while(n>0):
        f=f*n
        n=n-1
    return f
x=int(input("enter number"))
f=fact(x)
print("factorial=%d"%f)
#2.
# input=[1,2,3,4,5],[10,20,30,40,50]
#output=[10,40,90,160,250]
lst1=[1,2,3,4,5]
lst2=[10,20,30,40,50]
for i in lst1:
    for j in lst2:
        lst=list(map(lambda i,j:i*j,lst1,lst2))
print(lst)
#3.print common elements of both list.
list1=[]
list2=[]
n=int(input("enter total number"))
for i in range(n):
    list1.insert(i,int(input()))
for i in range(n):
    list2.insert(i,int(input()))
print(list1)
print(list2)
lst=list(filter(lambda k:k in list1,list2))
print(lst)
#4.enter list and find cube of elements using functions.
n=int(input("enter number"))
list1=[]
for i in range(n):
    list1.insert(i,int(input()))
print(list1)
for i in list1:
    lst=list(map(lambda i:i**3,list1))
print(lst)
#5.input=[-1,2,-3,5,7,8,9,-10]
#output=[2,5,7,8,9,-10,-3,-1]
list1=[-1,2,-3,5,7,8,9,-10]
positive=list(filter(lambda i:i>0,list1))
negative=list(filter(lambda i:i<0,list1))
positive.sort()
negative.sort()
positive.extend(negative)
print(positive)'''
#6.add elements of two list in new list and calculate total
from functools import reduce
lst1=[]
lst2=[]
n=int(input("enter number"))
for i in range(n):
    lst1.insert(i,int(input()))
for j in range(n):
    lst2.insert(j,int(input()))
print(lst1)
print(lst2)
lst=list(map(lambda i,j:i+j,lst1,lst2))
print(lst)
lt=list(map(lambda i,j:i-j,lst1,lst2))
print(lt)
total=reduce(lambda a,b:a+b,lst)
print(total)