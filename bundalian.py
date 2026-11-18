# ========================================
# INFORMATION AND INTEGER CALCULATOR
# ========================================

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nHello,", name)
print("Your age is", age)

# Check the age
if age >= 18:
    print("You are already an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are still young.")

# Variables and data typesma
number1 = 20
number2 = 5
message = "Learning Python"
is_learning = True

print("\n===== MY VARIABLES =====")
print("Number 1:", number1)
print("Number 2:", number2)
print("Message:", message)
print("Learning:", is_learning)

# Arithmetic operators
print("\n===== MATH OPERATIONS =====")

print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("Multiplication:", number1 * number2)
print("Division:", number1 / number2)
print("Floor Division:", number1 // number2)
print("Modulus:", number1 % number2)
print("Exponent:", number1 ** number2)

# PEMDAS
answer = 10 + 5 * 2
print("PEMDAS Answer:", answer)

# Relational operators
print("\n===== COMPARISON =====")

print(number1 == number2)
print(number1 != number2)
print(number1 > number2)
print(number1 < number2)
print(number1 >= number2)
print(number1 <= number2)

# Logical operators
print("\n===== LOGICAL OPERATORS =====")

print("AND:", age >= 13 and age <= 18)
print("OR:", age < 13 or age > 18)
print("NOT:", not is_learning)

# Add integers until the user enters zero
print("\n===== ADD NUMBERS =====")

total = 0
count = 0

while True:

    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        print("You entered zero.")
        break

    total = total + num
    count = count + 1

    if num > 0:
        print("This is a positive number.")

    elif num < 0:
        print("This is a negative number.")

    # Check if the number is even or odd
    if num % 2 == 0 and num > 0:
        print("It is an even number.")

    elif num % 2 != 0 or num < 0:
        print("It is odd or negative.")

    print("Your current total is:", total)

# Show the final answer
print("\n===== FINAL RESULT =====")

print("Name:", name)
print("Total:", total)
print("Number of numbers:", count)

if count > 0:
    average = total / count
    print("Average:", average)

else:
    print("No numbers were added.")

print("Thank you po")
