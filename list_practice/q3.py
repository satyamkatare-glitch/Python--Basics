
# Question : Find the greatest element and print its index too.

l = [12,102,18,1,0,497,89]

greatest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > greatest:
        greatest = l[i]
        index = i
   
print(f"Your greatest element is {greatest} at index {index}")