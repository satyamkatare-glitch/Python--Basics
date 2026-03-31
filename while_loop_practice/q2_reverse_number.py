
# Question : Accept a number and print it reverse.

num = int(input("tell me your Number :  "))

digit = 0
rev_num = 0

while num > 0:
    digit = num % 10
    num = num // 10
    rev_num = rev_num * 10 + digit
    
print(rev_num)
