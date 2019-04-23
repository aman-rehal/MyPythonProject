text = raw_input("Enter a string to evaluate ")

vowelCount = 0

for ch in text :
    if ch in "aeiou" :
        vowelCount = vowelCount + 1

