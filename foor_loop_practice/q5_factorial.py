
# Question : Factorial of a number.

num = int(input("tell me your number : "))

fact = 1

for i in range(1,num+1):

    print(f"{fact}*{i} = {fact*i}")

    fact = fact*i
    

print(f"Your factorial of {num}! is {fact}")
