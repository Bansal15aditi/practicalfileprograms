#1.create a nested dictionary
dict={}
n=int(input("enter total number of elements"))
for i in range(n):
    k=int(input("enter key"))
    dict[k]={}
    k1=int(input("enter keys"))
    v=int(input("enter value"))
    dict[k].update({k1:v})
print(dict)
#2. create a dictionary in form of{n:n**2}
dict={}
n=int(input("enter total number of elements"))
for i in range(1,n+1):
    k=i
    v=i**2
    dict.update({k:v})
print(dict)
#3. program to find whether inputted key is present in dictionary or not.
k1=int(input("enter any key number"))
dict={}
n=int(input("enter total number of elements"))
for i in range(n):
    k=int(input("enter key"))
    v=int(input("enter value"))
    dict.update({k:v})
print(dict)
if k1 in dict.keys():
    print("key is present")
else:
    print("key is not present")
#4. merge two nested dictionary
dict1={}
dict2={}
n=int(input("enter total number of elements"))
for i in range(n):
    k1=int(input("enter key"))
    dict1[k1]={}
    k=int(input("enter key no."))
    v=int(input("enter value"))
    dict1[k1].update({k:v})
for j in range(n):
    k2=int(input("enter key"))
    dict2[k2]={}
    K=int(input("enter keys"))
    V=int(input("enter value"))
    dict2[k2].update({K:V})
print(dict1)
print(dict2)
dict1.update(dict2)
print(dict1)
#5.create a dict. for marks of students in subjects.
dict1={}
n=int(input("enter total number of students"))
for i in range(n):
    k=int(input("enter number of students"))
    dict1[k]={}
    m=int(input("enter total subject"))
    for j in range(m):
        s=input("enter subject name")
        m=int(input("enter marks"))
        dict1[k].update({s:m})
print(dict1)