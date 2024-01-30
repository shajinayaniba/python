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

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Its prime")
    else:
        print("not prime")

n = int(input("check this number :"))
prime_checker(number=n)
