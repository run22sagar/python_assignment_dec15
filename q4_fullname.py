full_name = input("Enter your full name: ")
name = full_name.split()
count = len(name)

if count == 2:
    f_name, l_name = name
    print("First Name is {}".format(f_name))
    print("Last Name is {}".format(l_name))
if count == 3:
    f_name, mid_name, l_name = name
    print("First Name is {}".format(f_name))
    print("Middle Name is {}".format(mid_name))
    print("Last Name is {}".format(l_name))