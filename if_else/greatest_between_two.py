
# Question : Accept two number and print the greatest between them.

num1 = int(input("Enter your first number -"))
num2 = int(input("Enter your second number -"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")

elif num1 == num2:
     print(f"{num1} is equal to {num2}")
    
else:
     print(f"{num2} is greater than {num1}")
