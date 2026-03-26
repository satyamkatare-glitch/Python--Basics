
# Question : Take a number as input and print its table.

n = int(input("Which table do you want :- "))

count = 0

for i in range(n,n*10+1,n):
    count += 1
    print(f"{n} * {count} = {i}")