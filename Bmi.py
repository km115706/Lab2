def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI=weight/(height * height)
    print("Your BMI = ", BMI)
    print("====================================")
    if BMI < 18.5:
        print("under weight")
    elif 18.5 <= BMI <= 25.0:
        print("Normal Weight")
    else:
        print("Over weight")
calculate_bmi(weight=57, height=1.73)