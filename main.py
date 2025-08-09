import math
print("select an operation to perform: ")
print("1 ADD")
print("2 Subtract")
print("3 Multiplication")
print("4 Division")
print("5 Square root")
print("6 Square")

operation_str = input()
operation = int(operation_str)

if operation == 1:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    Total= int(num1) + int(num2)
    print("The total of two numbers is:"+ str(Total))

elif operation == 2:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    Difference = int(num1) - int(num2)
    print("The difference of two numbers is:" + str(Difference))
elif operation == 3:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    Product = int(num1) * int(num2)
    print("The Product of two numbers is:" + str(Product))
elif operation == 4:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    Result = int(num1) / int(num2)
    print("The Result of two numbers is:" + str(Result))
elif operation == 5:
    num = input("Enter number to find  square root of : ")
    Result = math.sqrt(int(num))
    print("Result of the square root of the  number:",Result)
elif operation == 6:
    num = input("Enter number to find the square  of : ")
    Result = int(num)*int(num)
    print("Result of the square of the number:",Result)
else:
    print("Invalid Entry")