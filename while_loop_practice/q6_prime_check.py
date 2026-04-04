
# Question : Check prime number. 

n = int(input("tell me your number : "))

i = 2
is_prime = True

while i <= n // 2:
    if n % i == 0:
        is_prime = False
        break
    
    i += 1

if is_prime and n > 1:
    print("Prime number")

else:
    print("Not Prime")

