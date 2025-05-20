print("Class Register\n")

names = []
ages = []

while True:
    name = input('Enter your name (or type "done" to finish): ').strip().lower()
    if name == 'done':
        break
    age = input('Enter your age (or type "done" to finish): ').strip().lower()
    if age == 'done':
        break
    try:
        age = int(age)
        names.append(name)
        ages.append(age)
    except ValueError:
        print("Please enter a valid integer for age.")

students = list(zip(names, ages))

print("\nStudent List:")
for idx, (name, age) in enumerate(students, start=1):
    print(f"Student {idx}: {name.capitalize()}: {age} years old.")
