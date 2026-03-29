
# Question : Count all letters, digits, and special symbols from given string.

str = input("Enter yor string by using letters, digits, and special symbols :-  ")

chars = 0
digits = 0
symbols = 0



for i in str:
    if i.isalpha():
        chars += 1

    elif i.isdigit():
        digits += 1

    else:
        symbols += 1

print(f"Your letters in this string are {chars}\nYour digits in this string are {digits}\nYour special symbols in this string are {symbols}")

