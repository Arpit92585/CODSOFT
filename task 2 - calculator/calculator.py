print("Welcome to the calculator")
print("Enter the first number")
num1 = int(input())
print("Press '+','-','*','/'")
op = input()
print("Enter the second number")
num2 = int(input())

if op == "+":
  print(num1 + num2)

elif op == "-":
  print(num1 - num2)

elif op == "*":
  print(num1 * num2)

elif op == "/":
  print(num1 / num2)

else:
  print("Choose the correct operation")