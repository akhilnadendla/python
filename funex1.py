def larg(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest = num1
    elif (num2 > num1) and (num2 > num3):
        largest = num2
    else:
        largest = num3
    return [largest]


print(larg(10, 20, 30))
print(larg(1, 20, 3))
print(larg(10, 2, 30))