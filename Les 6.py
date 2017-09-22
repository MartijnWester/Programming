weight = float(input('Enter your weight in pounds: '))
height = float(input('Enter your height in inches: '))
def BMI(weight, height):
    bmi = (weight*703) / height**2
    print(bmi)
    if bmi < 18.5:
        print("Je hebt ondergewicht")
    elif bmi > 25.0:
        print("Je hebt overgewicht")
    else:
        print("Je hebt een normaal gewicht")

BMI(weight, height)

