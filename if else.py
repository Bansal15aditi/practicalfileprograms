#1. check input string is palindrome or not.
str=input("enter string")
str1=str[::-1]
if(str==str1):
    print("string is palindrome")
else:
    print("string is not palindrome")
#2. check whether the input character is vowel or consonent.
str=input("enter character")
if(str=='a' or str=='e' or str=='i' or str=='o' or str=='u' or str=='A' or str=='E' or str=='I' or str=='O' or str=='U'):
    print("character is vowel")
else:
    print("character is consonent")
#3. check number is positive, negative or zero
n=int(input("enter number"))
if(n>0):
    print("number is positive")
elif(n<0):
    print("number is negative")
else:
    print("number is zero")
#4. check triangle is valid or not
a=int(input("enter first angle"))
b=int(input("enter second angle"))
c=int(input("enter third angle"))
if(a>0 and b>0 and c>0 and a+b+c==180):
    print("valid triangle")
else:
    print("invalid triangle")
#5. check whether input character is alphabet,digit or special character.
ch=input("enter character")
if(ch>='A' and ch<='Z' or ch>='a' and ch<='z'):
    print("character is alphabet")
elif(ch>='0' and ch<='9'):
    print("character is digit")
else:
    print("special character")