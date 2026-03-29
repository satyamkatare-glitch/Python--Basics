
# Question : Check a string is pallindrome or not.

str = input("check your string is Pallindrome or not :- ")

rev = ""

for i in range(len(str)-1,-1,-1):
    rev += str[i]

if rev == str:
    print("Yes your string is Pallindrome")

else:
    print("No your string is not Pallindrome")
