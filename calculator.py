
# Interactive Calculator and Unit Converter

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


# Validate number input
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


# Main menu
while True:
    print("\n=== Interactive Calculator & Unit Converter ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Kilometres to Miles")
    print("6. Celsius to Fahrenheit")
    print("7. Currency Converter")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    # Validate menu choice
    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid choice! Please select 1-8.")
        choice = input("Choose an option (1-8): ")

    if choice == "8":
        print("Thank you for using the calculator!")
        break

    elif choice in ["1", "2", "3", "4"]:
        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        else:
            print("Result:", divide(a, b))

    elif choice == "5":
        km = get_number("Enter distance in kilometres: ")
        miles = km * 0.621371
        print("Distance in miles:", round(miles, 2))

    elif choice == "6":
        celsius = get_number("Enter temperature in Celsius: ")
        fahrenheit = (celsius * 9 / 5) + 32
        print("Temperature in Fahrenheit:", round(fahrenheit, 2))

    elif choice == "7":
        print("1. INR to USD")
        print("2. USD to INR")

        currency_choice = input("Choose conversion (1-2): ")

        while currency_choice not in ["1", "2"]:
            print("Invalid choice! Enter 1 or 2.")
            currency_choice = input("Choose conversion (1-2): ")

        amount = get_number("Enter amount: ")

        # Example rates only; update with the current exchange rate.
        inr_to_usd = get_number("Enter current INR-to-USD rate: ")

        if inr_to_usd <= 0:
            print("Exchange rate must be greater than zero.")
        elif currency_choice == "1":
            print("Amount in USD:", round(amount * inr_to_usd, 2))
        else:
            print("Amount in INR:", round(amount / inr_to_usd, 2))
