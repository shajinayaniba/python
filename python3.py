#print("I love you abinaya, I love di pondatii")
#height = int(input("Enter the height in cm:  "))
#if height >= 170:
#  print("He is eligible")
#else:
#  print("Not eligible")

#To find odd or even
#number = int(input("enter the number to find odd or even:  "))
#if number % 2 == 0:
#    print("even number")
#else: 
#    print("odd number")  

#Nested if statme
height = float(input("Enter the height in cm:  "))
age = float(input("Enter your age"))
bill = 0
if height >= 170:
 print("He is eligible")
 if age < 12:
  bill = 10
  print("Pay 10 rupees")
 elif age <=18:
  bill = 20
  print("Pay 20 rupees")
 else:
  bill =30
  print("pay 30 rupees")
  wantphoto = input("Want photo yes or no ")
  if wantphoto == "yes":
   bill += 3
   print(f"your bill is {bill}")
   
else:
  print("Not eligible") 
# 
#  BMI Calculator
# height = float(input("enterr your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / height **2)
# if bmi < 18.5:
#  print(f"your bmi is {bmi} ,you are underweight.")
# elif bmi < 25:
#  print(f"your bmi is {bmi} ,you are normalweight.")
# elif bmi < 30:
#  print(f"your bmi is {bmi} ,you are overweight.")
# elif bmi < 35:
#  print(f"your bmi is {bmi} ,you are obese.")
# else:
#  print(f"your bmi is {bmi} ,you are clinically obeseee.")