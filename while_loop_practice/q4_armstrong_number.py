
# Question : Check Armstrong Number. (Number = sum of digits^power) 

num = int(input("Tell me your number : "))

n = num
power = len(str(n))

digit = 0
sum_digit = 0
sum_digit_int = int(sum_digit)

while num > 0:
    digit = num % 10
    sum_digit +=  digit ** power
    num = num // 10

print(sum_digit)

if sum_digit_int == num:
    print("Armstrong")
else:
    print("Not Armstrong")

