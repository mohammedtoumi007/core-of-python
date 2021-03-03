
# *******exemple output*******
print("Hello world")
###############################
print("The numbers are : %5d: %010d" %(5,-20))
###############################
name = "sam"
score = 90
print("Total score for %s is %s"%(name,score))
###############################
print ("{:3} {:6} {:10} {:12}".format("a", "bc","def","gh"))
###############################
word = 'word'
sentence ="This is a sentance"
paragraph = """This is a paragraph. iT is made up of miltiple lines and sentences,"""
print(word, sentence, paragraph)

# *******exemple intput*******

age = input("Age?")
print(age)
###############################
Names = input("Please enter the names")
print(Names)

# *******If Conditional*******

a,b=1,10
if a>b:
    print("a>b")
elif a<b:
    print("a <b")
else :
    print("a = b")
###############################
a,b = 1,10
max = a if (a>b) else b
print(max)
###############################
if 'a' in ['b','c','a']:
    print ("a in the list")
else: print ("a not in the list")

# *******loops*******

i=0
while i<4 :
    print(i)
    i+=1
###############################
while True:
    a= input('>')
    if a=="exit":
        break
    print(a)
###############################
for a in range(3):
    print(a)
###############################
for a in range(1,6,2):
    print(a)
###############################
for item in ['jordan','US','UK']:
    print(item)

# *******Lambda, filtering & Mapping*******
# Lambda : Inline anonymous function (Not bounded to a name)
# Filter : Filter out all the elements of a sequence
# Map : Applies a function to all teh items in a sequence

sum = lambda x,y : x+y
print(sum(56,7))

###############################

MyList = [0,1,2,3,4,10,13,22,25,100,120]
odd_numbers = list(filter(lambda x: x % 2, MyList))
print(odd_numbers)
even_numbers = list(filter(lambda x: x % 2 == 0, MyList))
print(even_numbers)
###############################

sentence = "university USA"
print(list(map(lambda word: len(word), sentence.split())))

# *******Reduce*******
product = 1
list = [1,2,3,4]
for num in list :
    product = product * num
print(product)

###############################

from functools import reduce
product = reduce((lambda x, y: x*y),[1,2,3,4])
print(product)

# *******Generators*******
def generator_function():
    for i in range(10):
        yield i
for item in generator_function():
    print(item)
###############################

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b,a+b
for x in fibon(120):
    print(x)

# *******Exceptions Handling*******
while True:
    try:
        n = input("Please enter an integer :")
        n = int(n)
        break
    except ValueError :
        print("No valid integer! Please try again...")
print("Great, you successfully entered an integer !")
###############################

try:
    x = float(input("your number:"))
    inverse = 1.0/x
except ValueError :
    print("You should have given either en int or a float")
except ZeroDivisionError :
    print("Infinity")
finally :
    print("There may or may not have been an exceptions.")

# *******Recursive Functions*******

def factorial(n):
    if n==1:
        return 1
    else :
        return n * factorial(n-1)
factorial(10)

# *******String*******
var1 = "Hello world!"
var2 = "Python programming"
print("var1[0]:", var1[0])
print("var2[1:5]:", var2[1:5])
print("count(n) :" , var2.count("m"))
for c in "Hello": print(c)
print("len(var1) : ", var1, len(var1))
str1 = "Hello" + " "+ var2
print("str1",str1)
str2 = "%s %s %d" ("Hello", str1,12)
print("str2:",str2)

###############################
s="Hello"
print("s.capitalize() :", s.capitalize())
print("s.upper()",s.upper())
print("s.center()", s.center(20))
print("s.replace():", s.replace("l","(ell)"))
print("strip():","world".strip())