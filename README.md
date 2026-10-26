# interactive-calculator-unit-converter

Beginner-friendly Python calculator and unit converter CLI project

📌 Project Overview

The Interactive Calculator & Unit Converter is a beginner-friendly command-line application developed using Python. It performs basic arithmetic operations, converts units, and supports currency conversion between Indian Rupees (INR) and US Dollars (USD).

This project demonstrates fundamental Python concepts such as functions, conditional statements, loops, exception handling, and user input validation.

✨ Features

➕ Addition — Adds two numbers.

➖ Subtraction — Subtracts one number from another.

✖️ Multiplication — Multiplies two numbers.

➗ Division — Divides two numbers with division-by-zero handling.

📏 Kilometres to Miles — Converts kilometres into miles.

🌡️ Celsius to Fahrenheit — Converts temperature from Celsius to Fahrenheit.

💱 Currency Converter — Converts INR to USD and USD to INR using a user-provided exchange rate.

✅ Input Validation — Handles invalid menu choices and non-numeric inputs.

🔁 Interactive Menu — Allows users to perform multiple operations until they choose to exit.

🛠️ Technologies Used

Python 3

Functions

Conditional statements (if, elif, else)

Loops (while)

Exception handling (try-except)

User input and type conversion

📂 Project Structure

interactive-calculator-unit-converter/
│
├── calculator.py
└── README.md

🚀 Getting Started

Prerequisites

Install Python 3 on your computer.

Check your Python installation:

py --version

Installation

Clone this repository:

git clone https://github.com/YOUR-USERNAME/interactive-calculator-unit-converter.git

Navigate to the project folder:

cd interactive-calculator-unit-converter

Run the program:

py calculator.py

Replace YOUR-USERNAME with your actual GitHub username in the clone URL.

💻 Sample Output

=== Interactive Calculator & Unit Converter ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Kilometres to Miles
6. Celsius to Fahrenheit
7. Currency Converter
8. Exit

Choose an option (1-8): 1
Enter the first number: 10
Enter the second number: 5
Result: 15.0

Unit Conversion Example

Choose an option (1-8): 5
Enter distance in kilometres: 10
Distance in miles: 6.21

Currency Conversion Example

Choose an option (1-8): 7
Choose conversion (1-2): 1
Enter amount: 1000
Enter current INR-to-USD rate: 0.012
Amount in USD: 12.0

Note: The currency converter uses a manually entered exchange rate and does not fetch live market rates.

📚 Learning Outcomes

- Through this project, I practised:

- Writing and calling Python functions.

- Using conditional statements to select operations.

- Implementing while loops for repeated execution.

- Validating user input with try-except.

- Handling exceptional cases such as division by zero.

- Applying mathematical formulas for unit conversions.

🔮 Future Enhancements

- Integrate a live currency exchange rate API.

- Add more unit conversions, including kilograms to pounds.

- Improve the user interface and error messages.

- Add automated tests for all operations.

