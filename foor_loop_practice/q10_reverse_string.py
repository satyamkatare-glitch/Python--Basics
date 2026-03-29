
# Question : Reverse a string without using inbuild Functions.

str = input("Enter your string : ")

rev_str = " "

for i in range(len(str)-1,-1,-1):
    rev_str += str[i]
        
print(rev_str)