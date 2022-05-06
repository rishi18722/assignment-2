q1

str = str(input("Enter String: "))
print(len(str))
str = (str(input("Enter String: "))) [::-1]
print(str)
str = (str(input("Enter String: "))) [::-1]
print(str)
str = str(input("Enter String: "))
new_str= str[:10:] + "object oriented"
print(new_str)
 str = str(input("Enter String: "))
print(str.index('a'))
 str = str(input("Enter String: "))
print(str.replace(" ", ""))

q2

name = "Shashwat singh"
SID= "21109032"
department_name= "Production Engineering"
CGPA="10"
print("Hey, "+ name + "Here!")
print(" My SID is "+ SID)
print(" I am from "+ department_name + "department and my CGPA is "+ CGPA)

q3

a = 56
b = 10
print(a&b)


a = 56
b = 10
print(a|b)


a = 56
b = 10
print(a^b)


a = 56
b = 10
print(a<<2)
print(b<<2)


a = 56
b = 10
print(a>>2)
priont(b>>4)

q4

str = str (input( "Enter string: "))
if("name" in str):
    print("Yes")
else:
  print("No")
  
  q5
  
s1 = int(input("Enter Side 1: "))
s2 = int(input("Enter Side 2: "))
s3 = int(input("Enter Side 3: "))
if((s1 + s2) > s3):
    print("Yes")
elif((s2 + s3) > s1):
    print("Yes")
elif((s1 + s3) > s2):
    print("Yes")
else:
    print("No")
  
  q6
  
a=int(input("Enter first no"))
b=int(input("Enter second no"))

n=a^b
count=0
while n:
 count=count+1
 n=n&(n-1)

Print("no of bits to be flipped",count)
