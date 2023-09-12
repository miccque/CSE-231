VOWELS = "aeiou"
word = input("Enter a word ('quit' to quit): \n").lower()
while word != "quit":
    if word[0] in VOWELS:
        new_word = word + "way"
    else:
        for index,letter in enumerate(word):
            if word[index] in VOWELS:
                new_word = word[index:]+word[:index]+"ay"
                break
            if not any(letter in VOWELS for letter in word):
                new_word = word + "ay"
    print(new_word)
    word = input("Enter a word ('quit' to quit): \n").lower()