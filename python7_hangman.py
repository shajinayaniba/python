import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

guess = input("Enter the letter: ").lower()
for postion in range(word_length):
    letter = chosen_word[postion]
    if letter == guess:
        display[postion] = letter
    

