def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

print("Simple Calculator")
print("1. Add")
print("2. Subtract")

choice = input("Enter choice: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "1":
    print("Result:", add(num1, num2))
elif choice == "2":
    print("Result:", subtract(num1, num2))
else:
    print("Invalid input")
