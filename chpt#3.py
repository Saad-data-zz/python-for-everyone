#conditional Steps
"""x=5
if x < 10:
     print("Smaller")
if x > 20:
    print("bigger")
print("All Done")"""
"""The indenting is important when you use the if condition from the next line 
indentation which be more then 4 spaces otherwise the python gives you error"""
"""x=5
print("before 5")
if x ==5: # this "==" sign is bascially ask you that is this value equal to this value
    print("IS 5")
    print("Is Still 5")
    print("Third 5")"""
"""x=5
if x > 2:
    print("Bigger then 2")
    print("Still Bigger")
print("Done with 2") #this line is de indented which represents that i ended my block in line 19."""
#loop
"""for i in range(10):
    print(i)
    if i > 2:
        print("bigger then 2")
    print("Done with i", i)
print("All done")"""
#Nested Decisions
"""x=10
if x > 3:
    print("Bigger then 3")
    if x < 100:
        print("less then 100")
print("Complete")"""
#Abbove what we study is one way of decision
#now lets talk about the two way Decisions
"""x=4
if x > 5:
    print("bigger")
else:
    print("Smaller")
print("completed")"""
#Conditional Coding Part-2
#Here we are going to talk about the elif, In such kind of conditions only one condition works at teh same time.
"""x=9
if x < 8:
    print("x less then 8")
elif x>8:
    print("x bigger then 8")
else:
    print("Dont know")
print("Completed")"""
#as you can see only one condition run at the sametime
#Conditional Coding Part-2
"""x=5
if x < 2:
    print("greater then 2")
elif x > 6:
    print("x greater then 6")
else:
    print("nothing")"""
# Example when we dont use the option of the else,In Such type of Conditions no condition will be executed sometimes
#No Else
"""x=9
if x < 2:
    print("greater")
elif x < 8:
    print("greater then 8")
print(" non Executed")"""
# Concept of catching Air
"""das="hello Me"
try:
    asd= int(das)
except:
    print("-1")"""
#Sample to try the program
"""rawstr= input("Enter a number")
try:
    ival=int(rawstr)
except:
    ival = -1
if ival > 0:
    print("Nice work")
else:
    print("It's not a number")"""
#exp
"""astr ="Hello Bob"
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(istr)"""
#exp2
"""astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)"""
#3.1
"""hrs = input("Enter Hours:")
h = float(hrs)
xx = input("Enter the Rate:")
x = float(xx)
if h <= 40:
 	print( h  * x)
elif h > 40:
	print(40* x + (h-40)*1.5*x)
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F"""
#EXP.3.3
Score=input("Enter the Score:")
try:
    ss=float(Score)
except:
    print("Error, input value is not number, TRY AGAIN")
    quit()
if ss >=0.9:
    print("A")
elif ss >= 0.8:
    print("B")
elif ss >= 0.7:
    print("C")
elif ss >= 0.6:
    print("D")
elif ss < 0.6:
    print("F")
