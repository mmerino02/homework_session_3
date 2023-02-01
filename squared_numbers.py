print("This code finds the amount of numbers that squared have a product less than a determined upper bound")

print("") #leave an space between lines. If it's more than one do ("\n")

print("Enter the Upper bound (up)")
p=int(input("Enter a number: ")) #The int() function converts the specified value into an integer number.

print("")

n=1
while n**2<p:
    print(n,"x",n,"=",n**2)
    n+=1

print("")

print("There are",n-1,"numbers with a square product less than",p)
