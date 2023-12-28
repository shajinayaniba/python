import random
word_list = ["abinaya", "shajin"]
chosen_word = random.choice(word_list)
guess = input("Enter the word: ").lower
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")

