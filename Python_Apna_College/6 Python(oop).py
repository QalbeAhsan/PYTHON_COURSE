class MyClass:
    def __init__(self, name, post):
        self.name = name
        self.post = post

    def display_info(self):
        print(f" {self.name} Is a  {self.post}")

# Creating an instance(object) of MyClass
person= MyClass("Ahsan","Manager")

# Creating an instance(object) of MyClass
name=input("please enter your name:")
x=(input("please enter your post: "))
person1= MyClass(name,x)

#CREATING INSTANCE(OBJECT)OF CLASS
name=input("pkease enter your name:")
x=(input("please enter your post: "))
person2 = MyClass(name,x)

# Calling a method on the instance (of all three objects we have made)
person.display_info()
person1.display_info()
person2.display_info()



# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# Child class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Child class 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Another Child class
class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

# Example of polymorphism
def animal_sound(animal):
    print(animal.speak())

# Create instances of different animals
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Demonstrate polymorphism
animal_sound(dog)  # Output: Buddy says Woof!
animal_sound(cat)  # Output: Whiskers says Meow!
animal_sound(cow)  # Output: Bessie says Moo!


#ENCAPSUlATION
class Car:
    def __init__(self,name,color):  
        self.__name = name        #WE MAEK THE NAME AND COLOR PRIVATE 
        self.__color = color

    def details_car(self):
        print(f"{self.__name} {self.__color}")

    def set_color(self,color):    #WE ARE USING GET SET SO THAT BE ACCESIBLE OUTSIDE THE CLASS
        self.__color=color

    def get_color(self):
        print(f"{self.__color}") 
    

car1 = Car("Toyota","Black")
car1.get_color()    #HERE WE CALL GET METHOD TO PRINT COLOR DIRECT ACCESS NOT POSSIBLE