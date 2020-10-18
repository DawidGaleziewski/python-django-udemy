# classes should be capitalized
class Dog:

    # Creating class variable
    dogInfo = "Hey dogs are cool"

    # Adding methods to a class is same as declaring a function in it
    # When we use method it will add first param as a this object that we will init
    def bark(self, str):
        print('BAARK!' + str)

# Creating a instance of a class is just using the class name + ()
mydog = Dog()
mydog.bark(" Hooman!")

# class with params
class Cat:
    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor
    
    def describe(self):
        print('I am a cat that is {} years old, my fur is {} and you can call me {}'.format(self.age, self.furcolor, self.name))

mycat = Cat('Mittens', 23, 'Red')
mycat.describe()