
# Question : Check Strong Number. (factorial of digits ka sum = number)

n = int(input("Tell me your number : "))

original = n

sum = 0

while n > 0:
    digit = n % 10

    fact = 1
    i = 1

    while i <= digit:
        fact = fact * i
        i += 1

    sum += fact
    n = n // 10


if sum == original:
    print("Strong Number")

else:
    print("Not a strong number")