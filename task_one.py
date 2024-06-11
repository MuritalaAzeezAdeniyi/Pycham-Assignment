a = 0
b = 1
next_number = a


count = 0

while count <= 10:

    a,b = b, next_number
    print(next_number, end=', ')
    next_number = a + b
    count = count + 1




