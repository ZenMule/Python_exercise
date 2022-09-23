weight = float(input("What's your weight (lbs or kg)? "))
unit_wgt = input("Weight unit: lbs or kg? ")
height = float(input("What's your height (in or m)? "))
unit_hgt = input("Height unit: in or m? ")

if unit_wgt.lower() == "lbs":
    weight = weight / 2.205

if unit_hgt.lower() == "in":
    height = height / 39.37

bmi = round(weight / height ** 2, 1)
weight_idl_upr = round(24.9 * height ** 2, 1)
weight_idl_lwr = round(18.6 * height ** 2, 1)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, and you are underweight. (Given your height, your healthy range of weight should be {weight_idl_lwr}-{weight_idl_upr}kg.)")
elif bmi < 25:
    print(f"Your BMI is {bmi}, and you are healthy. (Given your height, your healthy range of weight should be {weight_idl_lwr}-{weight_idl_upr}kg.)")
elif bmi < 30:
    print(f"Your BMI is {bmi}, and you are overweight. (Given your height, your healthy range of weight should be {weight_idl_lwr}-{weight_idl_upr}kg.)")
else:
    print(f"Your BMI is {bmi}, and you are obese. (Given your height, your healthy range of weight should be {weight_idl_lwr}-{weight_idl_upr}kg.)")

if weight > weight_idl_upr:
    print(f"You should lose at least {round(weight-weight_idl_upr, 1)}kg to become healthy.")
elif weight < weight_idl_lwr:
    print(f"You should gain at least {round(weight_idl_lwr-weight, 1)}kg to become healthy.")
else:
    print("It's very healthy. Just keep it!")
    