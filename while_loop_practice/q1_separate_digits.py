
# Question : Separate each digit of a number and print it on the new line.

n = int(input("Tell me your number : "))

digit = 0

while n > 0:
    digit = n % 10
    n = n // 10
    # n = (n-digit) / 10
    print(digit)


