# Fill the arguments in the function.
def fun1(a, b=0, *args, **kwargs):
    print("a value: "+a)
    print("b value: ", b)
    print("args value: ", args)
    print("kwargs value: ", kwargs)


fun1("Hello", 0, 3, 10, 12, 20, author="Herman Melville", book="Moby Dick", year=1851)
