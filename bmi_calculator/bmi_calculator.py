print("You are at the right place! Let's check how fit you are and what you can do to be fitter.\n")
print("\nBMI CALCULATOR")

height = float(input("Enter your height in centimeter: "))
weight = int(input("Enter your weight in kilograms: "))
height_in_meters = height / 100

bmi = weight / (height_in_meters**2)

print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 19:
    print("Underweight, have nutritious food and gain more weight")
elif 19 <= bmi < 25:
    print("Normal weight, keep the same level")
elif 25 <= bmi < 30:
    print("Overweight, Alarming stage. hit gym and avoid junk food")
else:
    print("Obesity, It's important to consult a doctor for a personalized fitness plan and dietary guidance. ")
