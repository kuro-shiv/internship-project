import sys

def add(x, y): return x + y

def subtract(x, y): return x - y

def multiply(x, y): return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Choose 1/2/3/4/5: ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))
            except ValueError:
                print("Error: Enter numbers only.")
                continue

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
