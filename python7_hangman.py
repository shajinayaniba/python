import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Enter the letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)
