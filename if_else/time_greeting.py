
# Question : Time based greeting System

name = input("enter your name :- ").upper()
day = input("Enter your day :- ").upper()
time = int(input("Enter time (0-23) :- "))

if time >= 6 and time <= 12:
    print(f" {day}/{time}:00am Good Morning {name} ")

elif time > 12 and time <= 18:
    print(f"{day}/{time}:00apm Good Afternoon {name}") 

elif time > 18 and time <= 22:
    print(f"{day}/{time}:00pm Good Evening {name}")

else:
    print(f"{day}/{time}:00am Good Night {name}")



if day == "sunday":
    print(f"Enjoy your day {name}")
