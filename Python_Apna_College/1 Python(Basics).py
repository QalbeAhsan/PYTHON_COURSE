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





   #STRING INTERPOLATION 
x=(input("please enter the name "))
print(type(x))
print(len(x))

 
#NESTED LIST 
list=[1,2,3,['a','b',['aHSAN','hsan']]]
print(list[3][2][0])


#NESTED DICTONARIES 
dic={ 

    'ahsan':'husband',
     'atika':'wife',
    'children':{
      'baby1':'boy',
      'baby2':'girl'  
     }
    
     }

print(dic['children'])


#Operators  (false ,true :conditions )
print(1!=2 or 1>2)


#SLICING THE STRING 
name='ahsan'
print(name[-4:-1])
name='ahsan'
print(name[0:2])




#TO COUNT WORDS IN STRING 
def count_cat(s):
    count=0
    for word in s.lower().split():
        if word=='cat':
         count+=1
    return count
print(count_cat('cat are types of cat which cant be cat'))