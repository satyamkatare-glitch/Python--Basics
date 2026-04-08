
# Question : Check list is sorted or not.

l1 = [15,17,19,21,31,41,90]

l2 = [15,17,19,90,21,31,41]

# For loop in l1 
for i in range(len(l1)-1):
    if l1[i] < l1[i+1]:
        continue
    else:
        print("Your list L1 is not sorted")
        break
else:
    print("Your list L1 is sorted")

# For loop in l2
for i in range(len(l2)-1):
    if l2[i] < l2[i+1]:
        continue
    else:
        print("Your list L2 is not sorted")
        break
else:
    print("Your list L2 is sorted")