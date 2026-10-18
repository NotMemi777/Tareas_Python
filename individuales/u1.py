#7.6 Problem 6: Body Mass Index (BMI) and category flag
while True:
    try: 
        height = float(input("Type your height in Mts: "))
        weight = float(input("Type your weight in Kg: ")) 
        
        # Todo esto va dentro del try
        if weight <= 0 or height <= 0:
            print("Error: invalid input")
            continue  # Vuelve a pedir los datos si son negativos o cero
            
        break  # Si pasó la validación, rompe el ciclo y avanza
        
    except ValueError:
        print("Error: invalid input")

imc = weight/(height **2) 
is_underweight =  False 
is_normal = False
is_over_weight = False
print (f"Your IMC is: {imc:.2f}")

gender = input ("Type your gender (M/F): ").lower()
age = int (input("Type your age: "))

if gender == "f":
    fat_percentage = (1.20 * imc + (0.23 * age) - 5.4)
else: 
    fat_percentage = (1.20 * imc + (0.23 * age) - 16.2) 
    
print (f"Your fat percentage is: {fat_percentage:.2f}%")

if imc<18.5:
    is_underweight = True
elif   18.5 <= imc < 25.0:
    is_normal = True
elif imc >= 25:
    is_over_weight = True
    
print (f"is underweight: {is_underweight}")    
print (f"is normal: {is_normal}")    
print (f"is overweight: {is_over_weight}")