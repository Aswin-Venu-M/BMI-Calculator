print("Enter BMI :")
bmi = float(input())

if bmi < 16.0:
    print('Underweight (Severe Thickness)')
elif ((bmi >= 16.0) and (bmi <= 16.9)):
    print ('Underweight (Moderate Thickness)')
elif ((bmi >= 17.0) and (bmi <= 18,4)):
    print ('Underweight (Mid Thickness)')
elif ((bmi >= 18.5) and (bmi <= 24.9)):
    print ('Normal Range')
elif ((bmi >= 25.0) and (bmi <= 29.9)):
    print ('Oveweight (Pre-Obese)')
elif ((bmi >= 30.0) and (bmi <= 34.9)):
    print ('Obese (Class I)')
elif ((bmi >= 35.0) and (bmi <= 39.9)):
    print ('Obese (Class II)')
else:
    print ('Obese (Class III)')