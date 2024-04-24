def number(x):
    try:
        if(x>6):
            raise Exception()
        print(x)
    except:
        print("Exception Raised")


number(5)
number(7)