my_list = [4, 2, 4, 0, 2, 4, 5, 7, 8, 9, 23, 8, 5, 4, 2, 2, 34, 4, 45]
count = len(my_list)

min = my_list[0]
max = my_list[0]
for x in my_list:
    if x < min:
        min = x
    if x > max:
        max = x

print("Minimum number : {} and Maximum number : {}.".format(min, max))