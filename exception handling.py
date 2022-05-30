'''#1.input age of person check eligible for voting if not throw exception.
try:
    age=int(input("enter age"))
    if(age>=18):
        print("eligible for voting")
    else:
        raise ValueError
except ValueError:
    print("not eligible for voting")
#2. create file and check word exist in that file if not throw exception
try:
    f1=open("gla.txt",'w')
    str=input("enter string")
    f1.write(str)
    f1=open("gla.txt",'r')
    if(word in f1):
        print("word not found")
    else:
        raise NameError
except NameError:
    print("word not exist in file")
finally:
    print("file is craeted")
    f1.close()
#3. input angles of triangle and check valid if not throw exception.
try:
    a=int(input("enter first angle"))
    b=int(input("enter second angle"))
    c=int(input("enter third angle"))
    if(a>0 and b>0 and c>0 and a+b+c==180):
        print("valid")
    else:
        raise ValueError
except ValueError:
    print("triangle not valid")
#4. input number and positive if not throw exception.
n=int(input("enter number"))
try:
    if(n>0):
        print("no. is positive",n)
    else:
        raise ValueError
except Exception as e:
    print("no. is negative",e)'''
try:
    a=int(input("enter any number"))
    b=0
    c=a/b
    print(c)
except Exception as e:
    print("not divide by zero",e)

