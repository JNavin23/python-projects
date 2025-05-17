print("UNIT CONVERTER")

def kg_to_pounds(kg):
    return kg * 2.21

def pounds_to_kg(lb):
    return lb / 2.21

def celsius_to_fht(c):
    return (c * 9/5) + 32

def fht_celsius(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.62

def miles_to_km(miles):
    return miles / 0.62

def perform():
    print("Choose converter type:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilometers to Miles")
    print("6. Miles to Kilometers")

    values = int(input("Enter your choice (1-6): "))

    if values == 1:
        kg = float(input("Enter weight in Kilograms: "))
        print(f"{kg} kg = {kg_to_pounds(kg):.2f} pounds")
    elif values == 2:
        lb = float(input("Enter weight in Pounds: "))
        print(f"{lb} lb = {pounds_to_kg(lb):.2f} kilograms")
    elif values == 3:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fht(c):.2f}°F")
    elif values == 4:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fht_celsius(f):.2f}°C")
    elif values == 5:
        km = float(input("Enter distance in Kilometers: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles")
    elif values == 6:
        miles = float(input("Enter distance in Miles: "))
        print(f"{miles} miles = {miles_to_km(miles):.2f} kilometers")
    else:
        print("Invalid choice! Please select a number between 1 and 6.")

if __name__ == "__main__":
    perform()
