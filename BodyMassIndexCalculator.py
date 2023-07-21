#Body Mass Index Calculator

height = input("enter your height in m: ")

weight = input("enter your weight in kg: ")

#Basic equation is BMI = Weight(KG)/height^2(m^2)


BodyMassIndex = ((int(weight))/(float(height) ** 2))

BodyMassIndex = round(BodyMassIndex, 2)
print("Your body mass index is: " + str(BodyMassIndex))


