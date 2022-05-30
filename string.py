#1.program to reverse a string
str=input("enter string")
str1=str[::-1]
print("original string",str)
print("reverse string",str1)
#2. program to count alphabets,digits,special character in string
str=input("enter string")
a=0
d=0
s=0
for i in range(len(str)):
    if(str[i]>='a' and str[i]<='z' or str[i]>='A' and str[i]<='Z'):
        a+=1
    elif(str[i]>='0' and str[i]<='9'):
        d+=1
    else:
        s+=1
print("alphabets",a)
print("digits",d)
print("special character",s)
#3.create a string made from first,middle,and last character
str=input("enter string")
str1=""
t=len(str)
f=str[0]
l=str[-1]
m=str[t//2]
str1=str1+f+m+l
print(str1)
#4.check string is anagram or not
str1=input("enter first string")
str2=input("enter second string")
if(sorted(str1)==sorted(str2)):
    print("string are anagram")
else:
    print("strings are not anagram")
#5. reverse string words.
str=input("enter string")
str1=str.split()
print(str1)
str1.reverse()
print(str1)