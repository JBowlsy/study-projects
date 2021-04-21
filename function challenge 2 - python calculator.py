#functions challenge 2 - python calculator


#define functions for calculator

def addition(first_n, second_n):
    """create addition code"""
    added = round(first_n + second_n, 4)
    print("The sum of " + str(first_n) + " and " +str(second_n) + " is " + str(added))
    return str(first_n) + " + " + str(second_n) + " = " + str(added)

def subtraction(first_n, second_n):
    """create subtraction code"""
    subtracted = round(first_n - second_n, 4)
    print("The difference between " + str(first_n) + " and " +str(second_n) + " is " + str(subtracted))
    return str(first_n) + " - " + str(second_n) + " = " + str(subtracted)

def multiplication(first_n, second_n):
    """create multiplication code"""
    multiplied = round(first_n * second_n, 4)
    print("The multiplication of " + str(first_n) + " and " + str(second_n) + " is " + str(multiplied))
    return str(first_n) + " * " + str(second_n) + " = " + str(multiplied)

def division(first_n, second_n):
    """create division code"""
    if second_n != 0:
        divided = round(first_n/second_n, 4)
        print("The  between " + str(first_n) + " and " +str(second_n) + " is " + str(divided))
        return str(first_n) + " / " + str(second_n) + " = " + str(divided)
    else:
        print("Division error, cannot divide a number by 0")

def exponentiation(first_n, second_n):
    """create exponentiation code"""
    expon = round(first_n ** second_n)
    print(str(first_n) + " raised to the power of " +str(second_n) + " is " + str(expon))
    return str(first_n) + " ** " + str(second_n) + " = " + str(expon)

#welcome message
print("welcome to the python calculator app")

history = []

calculating = True
while calculating:
    first_n = float(input("\nEnter a number: "))
    second_n = float(input("Enter a number: "))
    operation = input("\nWhat type of operation would you like to perform (addition, subtraction, multiplication, division, or exponentiation: ").lower()


    if operation == "addition" or operation == "a":
        result = addition(first_n, second_n)
    elif operation == "subtraction" or operation == "s":
        result = subtraction(first_n, second_n)
    elif operation == "multiplication" or operation == "m":
        result = multiplication(first_n, second_n)
    elif operation == "division" or operation == "d":
        result = division(first_n, second_n)
    elif operation == "exponentiation" or operation == "e":
        result = exponentiation(first_n, second_n)        
    else:
        print("\nInvalid operation selection")
        result = "operation error"

    history.append(result)

#get user input as to whether they want to do another operation
        
    again = input("\nwould you like to perform another operation (y/n): ").lower()
    if again != "y":
        print("Calculation summary")
        for i in history:
            print(i)
        calculating = False
        print("Thanks for using the python calulator app")










