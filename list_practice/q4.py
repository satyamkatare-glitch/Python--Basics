
# Question : Find the second largest element

l = [120000,230,43,56,2900,126,21,456,243,4567,4567,2727]

# Here ( -inf ) is represents a value that is smaller than every possible number
largest = float('-inf')
sec_largest = float('-inf')
index = 0

for i in range(len(l)):
    
    if l[i] > largest:
        sec_largest = largest
        largest = l[i]

    elif l[i] > sec_largest and l[i] != largest:
        sec_largest = l[i]
        index = i

print(f"Your second largest element is {sec_largest} at index {index}")