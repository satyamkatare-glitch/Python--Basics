
# Question : Accept a year and check if it a leap year or not.

year = int(input("tell your year :- "))

if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")

elif year % 100 != 0 and year % 4 == 0:
    print(f"{year} is a leap year")

else:
    print(f"{year} is a normal year") 