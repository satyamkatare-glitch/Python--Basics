
# Question : Accept name and age from the user. Check if the user is valid voter or not.

name = input("Enter your Name first - ")

age = int(input("Enter your age to verify - "))

if age >= 18:
    print(f"Hello {name} you are a valid voter") 

else:
    print(f"Hello {name} your are not a valid voter you can vote after {18-age} years")