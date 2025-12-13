import art

print(art.logo)

def add(n1, n2):
    """Adds n1 and n2"""
    return n1 + n2

def subtrack(n1, n2):
    """Subtracks n2 from n1"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplys n1 with n2"""
    return n1 * n2

def divide(n1, n2):
    """Divides n1 to n2"""
    return n1 / n2

calculater_dictionary = {"+": add,
                         "-": subtrack,
                         "*": multiply,
                         "/": divide,
                         }
question = True
number1 = int(input("What's the first number? "))

while question:
    operation = input('Type a mathematical operator. "+", "-", "*" or "/" ')
    number2 = int(input("What's the second number? "))
    answer =  calculater_dictionary[operation](number1, number2)
    print(f"{number1} {operation} {number2} = {answer}")

    x = input("Dou you want to continue with the previous result or a new calculation?\n 'y' for continue and 'n' for new calculation. ")

    if x == "y":
        number1 = answer
    else:
        question = False
