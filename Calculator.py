Num1 = float(input("Enter your first number:  "))
Num2 = float(input("Enter your second number:  "))
op = input("Add(+), Subtract(-), Multiply(), or Divide(/):  ")

if op == "+":
    print(Num1 + Num2)
elif op == "-":
    print(Num1 - Num2)
elif op == "*":
    print(Num1 * Num2)
elif op == "/":
    print(Num1 / Num2)
else:
    print("Invalid operator entered!! Try Again")