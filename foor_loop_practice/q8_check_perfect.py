
# Question : Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself . EX - 6 = 1+2+3 = 6

n = int(input("tell me your number :- "))

factor = 0

for i in range(1,n):
    if n%i == 0:
        factor += i
    
if factor == n:
    print(f"Yes the number {n} is a perfect number")

else:
   print(f"NO the number {n} is not a perfect number")