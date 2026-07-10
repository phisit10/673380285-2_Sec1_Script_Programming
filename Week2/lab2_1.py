

num = float(input("What your number : "))

#print("helllo lab2 hi")
#print(num)5

if num > 0 : 
    print("your number is positive number ")
elif num < 0:
    print("your number is negative number ")
elif num == 0 :
    print("your number is ZERO")
else:
    print("invalid number")

evodd = num % 2

if evodd == 1 :
    print("your number is odd number")
elif evodd == 0 :
    print("your number is even number")
else:
    print("")

print("CHALENGE")

if num > 0 and evodd == 0 :
    print("your number is positive and even umber")
elif num > 0 and evodd == 1 :
    print("your number is positive and odd umber")
elif num < 0 and evodd == 0 :
    print("your number is negative and even umber")
elif num < 0 and evodd == 1 :
    print("your number is negative and odd umber")
elif num == 0 and evodd == 0 :
    print("your number is zero and even umber")
else:
    print("")

    
    

