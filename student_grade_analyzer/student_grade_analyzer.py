import csv
import json

def get_letter_grade(mark):
	if mark >= 90:
		return 'A+'
	elif mark >= 80:
		return 'A'
	elif mark >= 70:
		return 'B'
	elif mark >= 60:
		return 'C'
	elif mark >= 50:
		return 'D'
	else:
		return 'F'

def load_students():
	students = []
	csv_path = 'month1/projects/student_grade_analyzer/students.csv'
	try:
		with open(csv_path, newline='', encoding='utf-8') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				name = row['name']
				try:
					marks = int(row['marks'])
					if marks < 0 or marks > 100:
						print(f"Warning: Invalid marks for {name}. Skipping entry.")
						continue
				except (ValueError, KeyError):
					print(f"Warning: Invalid or missing marks for {name}. Skipping entry.")
					continue
				students.append({'name': name, 'marks': marks})
	except FileNotFoundError:
		print(f"Error: {csv_path} not found. Please check the file location.")
		exit(1)
	if not students:
		print("No valid student data found. Exiting.")
		exit(1)
	return students

def compute_stats(students):
	marks_list = []
	for s in students:
		marks_list.append(s['marks'])
	average = sum(marks_list) / len(marks_list)
	highest = max(marks_list)
	lowest = min(marks_list)
	return marks_list, average, highest, lowest

def assign_grades(students):
	for s in students:
		s['grade'] = get_letter_grade(s['marks'])


def save_report(students, average, highest, lowest):
	json_path = 'month1/projects/student_grade_analyzer/student_report.json'
	report = {
		'students': students,
		'average': average,
		'highest': highest,
		'lowest': lowest
	}
	with open(json_path, 'w', encoding='utf-8') as f:
		json.dump(report, f, indent=4)
	print(f'Report saved to {json_path}')

def show_menu():
	print("\nStudent Grade Manager Menu:")
	print("1. Show average marks")
	print("2. Show highest marks")
	print("3. Show lowest marks")
	print("4. Show all students with letter grades")
	print("5. Save report to JSON")
	print("6. Exit")


def main():
	students = load_students()
	marks_list, average, highest, lowest = compute_stats(students)
	assign_grades(students)

	while True:
		show_menu()
		choice = input("Enter your choice (1-6): ").strip()
		if not choice.isdigit() or not (1 <= int(choice) <= 6):
			print("Invalid choice. Please enter a number between 1 and 6.")
			continue
		if choice == '1':
			print(f"Average marks: {average:.2f}")
		elif choice == '2':
			print(f"Highest marks: {highest}")
		elif choice == '3':
			print(f"Lowest marks: {lowest}")
		elif choice == '4':
			print("\nStudent Grades:")
			for s in students:
				print(f"{s['name']}: {s['marks']} ({s['grade']})")
		elif choice == '5':
			marks_list, average, highest, lowest = compute_stats(students)
			assign_grades(students)
			save_report(students, average, highest, lowest)
		elif choice == '6':
			print("Exiting program.")
			break

if __name__ == "__main__":
	main()
