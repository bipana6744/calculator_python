#add
def sum(number1,number2):
    return number1 + number2
#subtract
def sub(number1,number2):
    return number1 - number2
#multiply
def multiply(number1,number2):
    return number1 * number2
#divide
def divide (number1,number2):
    return number1 / number2
# making dictionary to store operators

operation={
    "+":sum,
    "-":sub,
    "*":multiply,
    "/":divide,
    }
#displaying operator
def calculator():
    number1=float(input("enter the first number \n"))
    for symbol in operation:
        print (symbol)
    #ask user to choose the operator

    should_continue=True
    while should_continue: 
        operator=(input("Choose the operator\n"))
        number2=float(input("enter the second number\n"))
        calculation=operation[operator]
        answer=calculation(number1,number2)
        print(f"{number1} {operator} {number2} = {answer}")
        if input(f"type 'y to continue with {answer}")=="y":
            number1=answer    
            
        else:
            should_continue=False
            calculator()
calculator()
        
 