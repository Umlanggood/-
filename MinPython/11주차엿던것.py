def multiply(*args):
    sum = 1
    for i in args:
        sum *= i
    print(sum)

multiply(2,5)
multiply(2,2,5)
multiply(3,3,4,2)
multiply(3,5,10,2,3)
multiply(1,2,2,5,5,10)