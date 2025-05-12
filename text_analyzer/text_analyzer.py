print("TEXT ANALYZER")

text = input("Enter a text of your choice: ")
alphabets = []

text = text.lower()
alphabets.append(input("Enter the fist alphabet: ").lower())
alphabets.append(input("Enter the second alphabet: ").lower())
alphabets.append(input("Enter the third alphabet: ").lower())

print("\n")
print("ALPHABETS REPITIONS")

alphabets_repetition1 = text.count(alphabets[0])
alphabets_repetition2 = text.count(alphabets[1])
alphabets_repetition3 = text.count(alphabets[2])

print(f"We have found the letter {alphabets[0]} repeated {alphabets_repetition1}")
print(f"We have found the letter {alphabets[1]} repeated {alphabets_repetition2}")
print(f"We have found the letter {alphabets[2]} repeated {alphabets_repetition3}")

print("\n")
print("NUMBER OF WORDS")

words = text.split()
print(f"We have found {len(words)} words in your text")

print("\n")
print("FIRST AND LAST LETTERS")

first_letter = text[0]
last_letter = text[-1]
print(f"The starting letter is {first_letter}, and ending letter is {last_letter}")

print("\n")
print("INVERTED TEXT")

words.reverse()
inverted_text = ' '.join(words)
print(f"If we order your text backwards it will say ' {inverted_text}'")

print("\n")
print("SEARCHING FOR THE WORD MOUNTAIN")

is_mountain = 'mountain' in text
dic = {True: "was", False: "was not"}

print(f"The word 'Mountain' {dic[is_mountain]} found.")