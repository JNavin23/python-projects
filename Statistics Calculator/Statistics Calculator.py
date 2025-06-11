import statistics as stats

collected_numbers = []

print("Enter Number One by One, or 'done'!")

while True:
    user_input = input("Enter Number (or done): ")
    if user_input.lower() == 'done':
        break

    try:
        number = int(user_input)
        collected_numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.")

if not collected_numbers:
    print("No numbers were entered to calculate statistics.")
else:
    print("\n Statistics ")
    print("Numbers entered:", collected_numbers)

    try:
        print("Mean: ", stats.mean(collected_numbers))
    except stats.StatisticsError:
        print("Mean: Error - Could not calculate mean.")

    try:
        modes = stats.multimode(collected_numbers)
        if len(modes) == len(collected_numbers) and len(collected_numbers) > 0:
            print("Mode: No common mode found (all values unique).")
        elif modes:
            print("Mode(s): ", modes)
        else:
            print("Mode: Could not determine mode.")
    except stats.StatisticsError:
        print("Mode: Error - Could not calculate mode(s).")

    try:
        print("Median: ", stats.median(collected_numbers))
    except stats.StatisticsError:
        print("Median: Error - Could not calculate median.")
