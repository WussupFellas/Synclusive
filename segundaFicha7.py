weight = float(input("Enter your weight, in kilos: "))
height = float(input("Enter your height, in meters: "))

imc = round((weight) / (height ** 2), 1)

if(imc >= 40):
    print(" Your IMC is ", imc, ", and is considered Morbid Obesity.")
elif(imc <= 39.9 and imc > 34.9):
    print(" Your IMC is ", imc, ", and is considered Obesity Type 2.")
elif(imc <= 34.9 and imc > 29.9):
    print(" Your IMC is ", imc, ", and is considered Obesity Type 1.")
elif(imc <= 29.9 and imc > 24.9):
    print(" Your IMC is ", imc, ", and is considered Overweight.")
elif(imc <= 24.9 and imc > 18.5):
    print(" Your IMC is ", imc, ", and is considered Normal Weight.")
else:
    print(" Your IMC is ", imc, ", and is considered Underweight.")