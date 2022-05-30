#1. create a file input string and search a word in that file.
file=open("aditi.txt",'w')
str=input("enter string")
file.write(str)
word=input("enter word")
file=open("aditi.txt",'r')
str1=file.read()
if(word in str1):
    print("word found")
else:
    print("word not found")
file.close()
#2. create two files input strings and input word and search it in both file.
file1=open("aditi1.txt",'w')
str1=input("enter string")
file1.write(str1)
file2=open("aditi2.txt",'w')
str2=input("enter string")
file2.write(str2)
word=input("enter word")
file1=open("aditi1.txt",'r')
st1=file1.read()
file2=open("aditi2.txt",'r')
st2=file2.read()
if(word in st1):
    if(word in st2):
        print("word found")
else:
    print("word not found")
#3. create a file and replace a word in that file.
file=open("aditi.txt",'w')
str=input("enter string")
file.write(str)
file=open("aditi.txt",'r')
str1=file.read()
str1=str1.replace("agra","mathura")
print(str1)
file.close()
#4. count uppercase characters in string in file.
file=open("aditi1.txt",'w')
str=input("enter string")
file.write(str)
file=open("aditi1.txt",'r')
str1=file.read()
l=len(str1)
c=0
for i in range(l):
    if(str[i].isupper()):
        c+=1
print(c)
file.close()
#5. create a file and print longest word in that file in length.
file=open("aditi2.txt",'w')
str=input("enter string")
file.write(str)
file=open("aditi2.txt",'r')
str1=file.read()
str2=max(str1.split(),key=len)
print(str2)