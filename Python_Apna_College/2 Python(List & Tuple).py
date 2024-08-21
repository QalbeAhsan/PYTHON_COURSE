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

# Initialize an empty list to store fruits
fruits= []
print("Please enter the names of 7 fruits:")
for i in range(7):
    fruit = input(f"Enter fruit {i + 1}: ")
    fruits.append(fruit)
print("THE LIST YOU CREATED IS:")
print(fruits)



# Initialize an empty list to store marks
marks= []
print("Please enter the marks of 5 marks:")
for i in range(5):
    mark = int(input(f"Enter mark {i + 1}: "))
    marks.append(mark)
print("THE LIST YOU CREATED IS:")
marks.sort()
print(marks)


       #Tuple in Python
student=("a","b","c","d")
print(student)
print(student[2])  
student[2]='f'         #We cannot change value in tuple like list when you run it it will give error in line 24
print(student[2])