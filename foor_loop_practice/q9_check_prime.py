
# Question : Check wether the number is prime or not. 

n = int(input("Check your number is prime or not : "))

count = 0

for i in range(1,n+1):
    if n%i == 0:
        count += 1
    
if count == 2:
    print(f"Yes {n} is a prime number")
else:
    print(f"No {n} is not a prime number")
