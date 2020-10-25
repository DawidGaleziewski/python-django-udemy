# You use def keyword to define the function
def hello():
    print("hello world!")
    print("hello part 2")

hello()
hello()
hello()

# using params
def goodbye(name):
    print("Bye " + name)

goodbye('Jake')
goodbye('Annie')
goodbye('Mike')

# Default function params
# We can return values same as in js
def getInfo(name, age=18, city="unknown"):
    return print("{} is {} years old and his location is {}".format(name, age, city))

getInfo('Mark', 30, 'Warsaw')
getInfo('Teferi')
