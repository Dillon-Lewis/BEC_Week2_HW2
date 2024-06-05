# Task 1

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

#Task 2

first= int(input("Pick a number: "))
second = int(input("Pick a second number: "))
Operation = input("Pick an operation: Add, Subtract, Multiply, Divide ")
if Operation == "Add":
    print(add(first, second))
if Operation == "Subtract":
    print(sub(first, second))
if Operation == "Multiply":
    print(mult(first, second))
if Operation == "Divide":
    print(div(first,second))
