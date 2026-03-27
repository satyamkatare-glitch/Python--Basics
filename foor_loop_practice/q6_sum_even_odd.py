
# Questions : Print the sum of all even and odd numbers in a range separately.



start = int(input("Enter start : "))
end = int(input("Enter end : "))

even_num = 0
odd_num = 0

for i in range(start,end+1):
    if i%2 == 0:
        even_num += i
        
    else:
        odd_num += i     

print(f"Even sum {even_num}")
print(f"Odd sum {odd_num}")


