"""#loops
n=0
while n >0:
    print("lather")
    print("Rinse")
print("Dry off!")"""
"""while True:
    line = input(">")
    if line == 'done':
        break
    print(line)
print("Done")"""
# Basically this loop runs and check
#Another Example
"""while True:
    line = input('>')
    if line[0]=="#":
        continue
    if line == "done":
        break
    print(line)
print("Done")"""
#lecture 5.2
"""for i in [5,4,3,2,1]:
    print(i)
print("blastoff")"""
#for loop with strings
"""friends=["Aitsam", "Talha","Eimad"]
for friend in friends:
    print("Mera Us pe char", friend)
print("done")"""
#example 5.3 finding the largest value
"""largest =-1
print("Before",largest)
for num in [9,12,31,41,15,74,91,-99]:
    if num > largest:
        largest = num
        print(largest, num)
print("After", largest)"""
#5.4 Idioms of Loop
"""zork =0
print("Before", zork)
for num in [9, 41, 12, 3, 74, 15]:
    zork= zork+1
    print(zork, num)
print("after", zork)"""
#Summary in the loop
"""zork= 0
print('Beofre Zork', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork+thing
    print(zork, thing)
print("After Zork ", zork)"""
#finding the average
"""count=0
sum=0
print("before",count, sum)
for thing in [9, 41, 12, 3, 74, 15]:
    count=count+1
    sum=sum+thing
    print(count, sum, thing)
print("After",count, sum, thing)"""
#flitering in the loop
"""print("before")
for value in [9, 41, 12, 3, 74, 15, 20]:
    if value > 20:
        print("Greater Value", value)
    elif value < 20:
        print("Smaller Vaue", value)
    else:
        print("Equal Value")
print("After")"""
#using boolean Variable
"""found=False
print("Before",found)
for value in [9, 41, 12, 3, 74, 15]:
    if value ==3:
        found=True
    print(found, value)
print("After", found)"""
#find the smallest Value
"""smallest = None
print("Before",smallest)
for num in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = num
    elif num <smallest:
        smallest = num
        print(smallest, num)
print("After", smallest)"""
"""n = 5
while n > 0 :
    print(n)
print('All done')"""
"""tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)"""
"""n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')"""
"""smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)"""
"""zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)"""
#Example code
"""num= 0
tot_con= 0
while True:
    user1= input("Enter The Number:")
    if user1 == "done":
        break
    try:
        user_conv=float(user1)
    except:
        print("Invaild Input")
        continue
    print(user_conv)
    num= num+1
    tot_con=tot_con+user_conv
print("All Done")
print("Total of Input Value", tot_con,"Total Count of Input",num,"Average", tot_con/num)"""
#Assignment 5
"""largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
    except:
        print("Invaild input")
        continue
    if largest is None or largest < num:
        largest = num
    elif smallest is None or smallest > num:
        smallest = num
    print("Maximum is", largest)
    print("Minimum is", smallest)"""
largest = None
smallest = None
while True:
    val = input("Enter a number: ")
    if val == "done":
        break
    try:
        val = int(val)
        if largest is None or val > largest:
            largest = val
        elif smallest is None or smallest > val:
            smallest = val
    except:
        print("Invalid input")
        continue
print("Maximum is", largest)
print("Minimum is", smallest)