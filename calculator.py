#This is a simple 2 number calculator
a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = input("Enter the operation (+,-,/,*) : ")
if (c == '+'):
    print("The answer is ",a+b)
elif (c == '/'):
    print("The answer is ",a/b)
elif (c == '-'):
    print("The answer is ", a - b)
elif (c == '*'):
    print("The answer is ", a * b)
else:
    print("Wrong operation entered")
