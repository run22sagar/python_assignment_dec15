def incr(sal):
    a = []
    for x in sal:
        x += (23/100) * x
        a.append(x)
    return a

salary = [15000, 20000, 17000, 18900, 30000]
new_salary = incr(salary)
print(new_salary)