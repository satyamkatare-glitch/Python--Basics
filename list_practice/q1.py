
# Question : Print positive and negative elements of an list 


l = [2,3,1,-2,4,-5,-10]


print("Your positive elements are :- ")

for i in range(len(l)):
    if l[i] >= 0:
        print(l[i])

print("Your negative elements are :- ")

for i in range(len(l)):
    if l[i] < 0:
        print(l[i])
