import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Enter the letter: ").lower()
    for postion in range(word_length):
        letter = chosen_word[postion]
        if letter == guess:
            display[postion] = letter
    if "_" not in display:
        end_of_game = True
        print("you win")        
    

