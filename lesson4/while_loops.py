# Factorials with While Loops
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)


# Factorials with For Loops
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
for i in range(1,number+1):
    product *= i

# print the factorial of number
print(product)


# Count By
start_num = 10
end_num = 500
count_by = 5

# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)


# Count By check
start_num = 1000
end_num = 500
count_by = 5

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
    break_num = start_num
    while break_num != end_num:
        break_num += count_by
    result = break_num

print(result)


# Nearest Square
# Write a while loop that finds the largest square number less than an
# integerlimit and stores it in a variable nearest_square. A square number is
# the product of an integer multiplied by itself, for example 36 is a square
# number because it equals 6*6.

limit = 40

# write your while loop here
num = 0
while (num+1)**2 < limit:
    num += 1
    nearest_square = num ** 2

print(nearest_square)
