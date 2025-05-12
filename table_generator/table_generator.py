print("Welcome to the Multiplication Table Generator!\n")

def table_genrator(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

while True:
    try:
        num = int(input("Enter number of which need a table: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")


print("\n")

table_genrator(num)