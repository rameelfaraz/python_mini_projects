def get_number(prompt):
	while True:
		value = input(prompt).strip()
		if not value:
			print("Input cannot be empty.")
			continue
		try:
			return float(value)
		except ValueError:
			print("Invalid input. Enter a number.")

def get_integer(prompt):
	while True:
		value = input(prompt).strip()
		if not value:
			print("Input cannot be empty.")
			continue
		try:
			return int(value)
		except ValueError:
			print("Invalid input. Enter an integer.")
			
import math

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		return "Error: Division by zero"
	return a / b

def square(a):
	return a ** 2

def cube(a):
	return a ** 3

def power(a, b):
	return a ** b

def factorial(n):
	if n < 0:
		return "Error: Negative factorial"
	result = 1
	for i in range(1, n+1):
		result *= i
	return result

def mean(numbers):
	if not numbers:
		return "Error: Empty list"
	return sum(numbers) / len(numbers)

def median(numbers):
	if not numbers:
		return "Error: Empty list"
	numbers = sorted(numbers)
	n = len(numbers)
	mid = n // 2
	if n % 2 == 0:
		return (numbers[mid - 1] + numbers[mid]) / 2
	else:
		return numbers[mid]

def main():
	print("Welcome to Smart Calculator!")
	while True:
		print("\nSelect an operation:")
		print("1. Add")
		print("2. Subtract")
		print("3. Multiply")
		print("4. Divide")
		print("5. Square")
		print("6. Cube")
		print("7. Power")
		print("8. Factorial")
		print("9. Mean (list)")
		print("10. Median (list)")
		print("0. Exit")
		choice = input("Enter your choice: ").strip()
		if not choice:
			print("Input cannot be empty. Please enter a valid choice.")
			continue

		if choice == '0':
			print("Goodbye!")
			break
		elif choice == '1':
			a = get_number("Enter first number: ")
			b = get_number("Enter second number: ")
			print("Result:", add(a, b))
		elif choice == '2':
			a = get_number("Enter first number: ")
			b = get_number("Enter second number: ")
			print("Result:", subtract(a, b))
		elif choice == '3':
			a = get_number("Enter first number: ")
			b = get_number("Enter second number: ")
			print("Result:", multiply(a, b))
		elif choice == '4':
			a = get_number("Enter numerator: ")
			b = get_number("Enter denominator: ")
			print("Result:", divide(a, b))
		elif choice == '5':
			a = get_number("Enter number: ")
			print("Result:", square(a))
		elif choice == '6':
			a = get_number("Enter number: ")
			print("Result:", cube(a))
		elif choice == '7':
			a = get_number("Enter base: ")
			b = get_number("Enter exponent: ")
			print("Result:", power(a, b))
		elif choice == '8':
			n = get_integer("Enter number: ")
			print("Result:", factorial(n))
		elif choice == '9':
			numbers = []
			print("Enter numbers one by one. Type 'done' to finish:")
			while True:
				entry = input("Number (or 'done'): ").strip()
				if not entry:
					print("Input cannot be empty. Please enter a number or 'done'.")
					continue
				if entry.lower() == 'done':
					break
				try:
					numbers.append(float(entry))
				except ValueError:
					print("Invalid input. Please enter a number or 'done'.")
			print("Numbers entered:", numbers)
			print("Mean:", mean(numbers))
		elif choice == '10':
			numbers = []
			print("Enter numbers one by one. Type 'done' to finish:")
			while True:
				entry = input("Number (or 'done'): ").strip()
				if not entry:
					print("Input cannot be empty. Please enter a number or 'done'.")
					continue
				if entry.lower() == 'done':
					break
				try:
					numbers.append(float(entry))
				except ValueError:
					print("Invalid input. Please enter a number or 'done'.")
			print("Numbers entered:", numbers)
			print("Median:", median(numbers))
		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
	main()
