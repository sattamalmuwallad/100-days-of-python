from art import arts 
print(arts)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    if n1 < n2: return n2 - n1
    else: return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0: return "Error: Division by zero"
    else: return n1 / n2

functions = {"+","-","*","/"}


def operations(n1, n2):
    if func == "+":
        print(f"The sum of {n1} + {n2} = {add(n1, n2)}")
    elif func == "-":
            print(f"The subtraction of {n1} - {n2} = {subtract(n1, n2)}")
    elif func == "*":
            print(f"The multiplication of {n1} * {n2} = {multiply(n1, n2)}")
    elif func == "/":   
            print(f"The divison of {n1} / {n2} = {divide(n1, n2)}")
    else:
         print("Invalid operation. Please choose from +, -, *, /.")

n1 = int(input("What is the first number "))
func = input("What is the operation that u want to do? ")
n2 = int(input("What is the second number "))

operations(n1,n2)
