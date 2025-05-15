import random

print("Let everyone in the class give your name.\nWe will choose one person who will pay the bill for today's party...")

def get_names():
    names = []
    print("Enter the names (type 'done' when finished):")
    while True:
        name = input("Enter your name: ")
        if name.lower() == 'done':
            break
        if name.strip():
            names.append(name.strip())
    return names

def unlucky_winner():
    names = get_names()
    if not names:
        print("No names entered!")
        return
    winner = random.choice(names)
    print(f"The unlucky winner who will pay the bill is: {winner}")

unlucky_winner()




