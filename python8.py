# #AREA CALCULATION

# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_cans = round(area / cover)
#     print(f"you will need {num_of_cans} cans")

# test_h = int(input("Height of wall :"))
# test_w = int(input("Width of wall : "))
# coverage = 5
# paint_calc(height = test_h, width = test_w, cover = coverage)

# PRIME NUMBER CHECKER

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("Its prime")
#     else:
#         print("not prime")

# n = int(input("check this number :"))
# prime_checker(number=n)



#Ceaser cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Encode or Decode")
text = input("Typer your message").lower()
shift = int(input("Type the shift number"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        postion = alphabet.index(letter)
        new_positon = postion + shift_amount
        new_letter = alphabet[new_positon]
        cipher_text += new_letter
    print(f"The encoded code is {cipher_text}")

encrypt(plain_text=text, shift_amount=shift)
