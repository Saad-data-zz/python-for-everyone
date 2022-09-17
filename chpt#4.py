#function #def basically define the function
"""def thing():
    print("Hello")
    print("Fun") #this indentention defines that function block is finish
thing() #this line of code is to recall the store function
print("Zip")
thing()"""
#both thing() working as you can see in the output
#Max and Min Functions
"""big=max("Hello world")
print(big)
small=min("Hello world")
print(small)
#these function gives us the output of max adn min inthe given statement
#reture values
def greet():
    return "hello"
print(greet(), "Glenn")
print(greet(), "sally")"""
#better example for the return function
"""def greet(lang):
    if lang=="es":
        return "from es Hola"
    elif lang == "fr":
        return "from fr Bonjour"
    else:
        return "Hello"
print(greet("en"), "Glenn")
print(greet("fr"),  "Sally")
print(greet("es"), "Michael")"""
"""def thing():
    print('Hello')

print('There')"""
"""def func(x) :
    print(x)

func(10)
func(20)"""
"""def stuff():
    print('Hello')
    return
    print('World')

stuff()"""
"""def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')"""
""""def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)"""
#assignment#4.2
"""def computepay(h, r):
    return 498.75

hrs = input("Enter Hours:")
p = computepay(10, 20)
print("Pay", p)"""


def computepay(h, r):
    if h > 40:
        pay = 1.5 * r * (h - 40) + (40 * r)
    else:
        pay = h * r
    return pay


hrs = input("Enter Hours:")
hr = float(hrs)
rate = input("Enter rate per hour:")
ratef = float(rate)

pay = computepay(hr, ratef)
print("Pay",pay)