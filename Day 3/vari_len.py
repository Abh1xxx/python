def print_name(*names):
    print("The type of argument is ",type(names))
    print("print the passed arguments ")
    for name in names:
        print(name)
    print_name('ABHI',"RAM","ADAM")