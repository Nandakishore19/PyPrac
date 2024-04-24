def calculator(op1,op2,operator):
    try:
        op1 = float(op1)
        op2 = float(op2)
    except ValueError:
        print("Non numeric Values were passed as arguments")
        return 
    
    try:
        if operator == '+':
            result= op1+op2
        elif operator == '-':
            result= op1-op2
        elif operator == '*':
            result= op1*op2
        elif operator =='/':
            if op2 ==0:
                raise ZeroDivisionError("Zero Division Not possible")
            result = op1/op2
        print(f"Result is {result}")
    except ZeroDivisionError as e:
            print(e)
    

calculator(1,2,'/')
calculator('a',2,'+')
calculator(1,0,'/')
