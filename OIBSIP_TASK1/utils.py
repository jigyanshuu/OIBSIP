def calculate_bmi(weight, height):
    return weight /(height**2)

def categorize_bmi(bmi):
    if bmi<18.5:
        return "Underweight"
    elif bmi<25:
        return "Normal"
    elif bmi< 30:
        return "Overweight"
    else:
        return "Obese"