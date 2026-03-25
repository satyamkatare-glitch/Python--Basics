
# Question : Driving Licence Eligibility Checker.

age = int(input("enter your age :- "))
test_passed = input("Test Passed (yes/no) : ").lower()

if age < 18:
    print("YOU are not Eligible")

else:
    if test_passed == "yes":
        print("Licence Approved")
    else:
        print("Retry test")

if age > 50:
    print("medical check required")

