import random
import string

def generate_password(length):
	letters = string.ascii_letters
	digits = string.digits
	symbols = string.punctuation

	if length <= 0:
		return ""

	all_chars = letters + digits + symbols

	if length < 3:
		return "".join(random.choice(all_chars) for _ in range(length))

	password_chars = [
		random.choice(letters),
		random.choice(digits),
		random.choice(symbols)
	]

	for _ in range(length - 3):
		password_chars.append(random.choice(all_chars))

	random.shuffle(password_chars)
	return "".join(password_chars)

def check_password_strength(password):
	feedback = []
	score = 0

	has_lower = any(char.islower() for char in password)
	has_upper = any(char.isupper() for char in password)
	has_digit = any(char.isdigit() for char in password)
	has_symbol = any(char in string.punctuation for char in password)

	if len(password) >= 8:
		score += 1
	else:
		feedback.append("Use at least 8 characters.")

	if len(password) >= 12:
		score += 1
	else:
		feedback.append("Use 12+ characters for better security.")

	if has_lower and has_upper:
		score += 1
	else:
		feedback.append("Mix uppercase and lowercase letters.")

	if has_digit:
		score += 1
	else:
		feedback.append("Add at least one number.")

	if has_symbol:
		score += 1
	else:
		feedback.append("Add at least one symbol (e.g., !, @, #, $).")

	if " " in password:
		feedback.append("Avoid spaces in passwords.")

	if score >= 5 and " " not in password:
		return "Strong", ["Great password."]
	if score >= 3:
		return "Medium", feedback
	return "Weak", feedback

def get_valid_length():
	MAX_LENGTH = 100
	while True:
		user_input = input("Enter password length: ").strip()
		if not user_input.isdigit():
			print("Please enter a positive whole number.")
			continue

		length = int(user_input)
		if length <= 0:
			print("Length must be greater than 0.")
			continue
		if length > MAX_LENGTH:
			print(f"Length must not exceed {MAX_LENGTH}.")
			continue

		return length

def main():
	while True:
		print("\n--- Password Tool ---")
		print("1. Generate Password")
		print("2. Check Password Strength")
		print("3. Exit")

		choice = input("Choose an option (1/2/3): ").strip()
		if not choice or not choice.isdigit():
			print("Invalid choice. Please select 1, 2, or 3.")
			continue

		if choice == "1":
			length = get_valid_length()
			password = generate_password(length)
			print(f"Generated password: {password}")
			strength, suggestions = check_password_strength(password)
			print(f"Strength: {strength}")
			if suggestions:
				print("Feedback:")
				for suggestion in suggestions:
					print(f"- {suggestion}")

		elif choice == "2":
			password = input("Enter password to check: ").strip()
			if not password:
				print("Password cannot be empty.")
				continue
			if all(c == ' ' for c in password):
				print("Password cannot be only spaces.")
				continue
			strength, suggestions = check_password_strength(password)
			print(f"Strength: {strength}")
			if suggestions:
				print("Feedback:")
				for suggestion in suggestions:
					print(f"- {suggestion}")

		elif choice == "3":
			print("Goodbye!")
			break

		else:
			print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
	main()
