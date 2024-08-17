#                         Task - 01 First  (" Calculator App ")          

def calculator():

    operation = input('''Please Type the mathe operation you would like to complete:
                  + for Addition
                  - for Subtraction
                  * for Multiplication
                  / for Division\n''')
    
    number1=float(input("Please Enter the First number:"))
    number2=float(input("Please Enter the Second number:"))

    if operation == '+':
        print("{} + {} = ".format(number1, number2))
        print(number1 + number2)

    elif operation == '-':
        print("{} - {} = ".format(number1, number2))
        print(number1 - number2)

    elif operation == '*':
        print("{} * {} = ".format(number1, number2))
        print(number1 * number2)

    elif operation == '/':
        print("{} / {} = ".format(number1, number2))
        print(number1 / number2)

    else:
        print("You have entered a wrong math operator:")
    again()

def again():
    calculation_again = input('''
Do you want to calculation again? Please type Y for Yes or N for No :
    ''')
    if calculation_again.upper() == 'Y':
        calculator()
    elif calculation_again.upper() == 'N':
        print("Bye Bye , Thank you for coming:")
    else:
        again()

calculator()
