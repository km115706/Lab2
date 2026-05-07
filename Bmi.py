def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI=weight/(height * height)
    print("Your BMI = ", BMI)
    print("====================================")
    if BMI < 18.5:
        print("under weight")
        return -1
    elif 18.5 <= BMI <= 25.0:
        print("Normal Weight")
        return 1
    else:
        print("Over weight")
        return 0
BMI_num=calculate_bmi(weight=57, height=1.73)
print (BMI_num)