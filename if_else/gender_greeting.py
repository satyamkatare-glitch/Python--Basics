
# Question: Accept gender and print greeting.

gender = input("Enter your Gender M/F - ")

male = "Good Morning SIR"
female = "Good Morning MAM"

if gender == "M" or gender == "m"  :
    print(male)

elif gender == "F" or gender == "f":
    print(female)

else:
    print("Unidentified gender")