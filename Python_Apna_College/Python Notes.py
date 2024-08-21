#LECTURE 1 FROM APNA COLLEGE

name=input("please enter your name:")
print("Welcome :",name)

age=input("please write your age :")
print("Your age is  :",age)

location=input("kindly write down your current location")
print("Your current location is :",location)

x=int(input("please give your first number :"))   #must see int word in this why we put this
y=int(input("kindly wite your second number:"))   #we do the explicit type conversion
sum=x+y
print("your final solution is ",sum)

           #practice to findout datatype 
print("your data type of varaible x is ",type(x))
print("your datatype for varaible location is :",type(location))

           #practice for operators
print("your sum of two numbers is")
print (x+y)           

#using logic operator 
print(x==y) #true false 


       #LECTURE 2 FROM APNA COLLEGE
       #Practice to find number is even or odd
num=int(input("please enter the number "))
print(num)
rem=num%2
if(rem==0):
    print("The number you put is EVEN")
else:
    print("The number you put is ODD")



    #To find greatest of three numbers 
num1=int(input("Write down your first number "))

num2=int(input("please write your second number "))

num3=int(input("Please write your third number"))

print("your selected numbers are:",num1,":",num2,":",num3)

if(num1>num2 and num1>num3):
 print("Your greatest number is :",num1)
elif(num2>num3):
   print("Your greatest number is :",num2)
else:
   print("Your greatest number is :",num3)


   
#FOR SIMPLE CALCULATOR
x=int(input("please give number 1:"))
y=int(input("please give number 2:"))
oper=input("Enter your operator")
if(oper=="+"):
    print(x+y)
elif(oper=="-"):
    print(x-y)
elif(oper=="*"):
    print(x*y)
else:
    print(x/y)        

    


    #List in phyton 
student=["a","b","c","d"]
print(student)
print(student[2])  
student[2]='f'          #Here we change the value of student index 2 
print(student[2])
print(type(student))   #we find type of student 
print(len(student))    #lenght of student 


     #taking numbers from user and put them in list 
numbers=[]
num1=int(input("first number"))
num2=int(input("second number"))
num3=int(input("third number"))
numbers=[num1,num2,num3]
print(numbers)


#Practice for the Dictionary in pythn
myinfo={
    "name":"ahsan",
    "age":"21",
    "location":"islamabad",
    "purpose":"internship"
}
print(myinfo)
print(type(myinfo))

#WE CAN ALSO PUT THE LIST OR TUPLES IN THE DICTIONARY LETS PRACTICE
Myinfo={
    "name":"ahsan",
    "members":["ahmad","afnan","hafeez"],
    "locations":["melsi","isb","lodhran"],
    "membersage":[16,15,55]
}
print(Myinfo["name"])
print(Myinfo["members"])
print(Myinfo["locations"])




Myinfo={
    "name":"ahsan",
    "members":["ahmad","afnan","hafeez"],
    "locations":("melsi","isb","lodhran"),
    "membersage":[16,15,55]
}
print(Myinfo)
Myinfo["members"][0] = "qari" # WE change value of key memeber ahmad value to qari
print(Myinfo["name"])         #if there will tuple inpace of list we cant change its value 
print(Myinfo["members"])
print(Myinfo["locations"])
