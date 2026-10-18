# ==========================================
# COVER PAGE
# ==========================================
# Name: Emilio Alejandro Becerra Mireles
# Student ID: 2630438
# Email: 2630438@upv.edu.mx
# Group: IM-1
# Assignment: Numeric types and booleans in Python

# ==========================================
# EXECUTIVE SUMMARY
# ==========================================
# Un int es un número entero (edad, horas) y un float tiene decimales
# (temperatura, sueldo). Si se mezclan en una cuenta, sale float.
# Un booleano solo vale True o False y sale de una comparación, como
# temp_c >= 30.0.
# Hay que revisar los rangos y que no se divida entre cero: con horas
# negativas o un ingreso de 0 el programa daría resultados absurdos.
# Aquí hay seis programas: temperaturas, horas extra, descuento,
# estadísticas de tres números, préstamo e IMC. Cada uno trae
# descripción, entradas, salidas, validaciones y tres casos de prueba.

# ==========================================
# GOOD PRACTICES
# ==========================================
# - Uso int para cosas que se cuentan y float para lo que lleva decimales.
# - Guardo los resultados de las cuentas en variables en vez de repetirlas.
# - Reviso los datos antes de calcular, por ejemplo que las horas no
#   sean negativas.
# - Uso nombres de variables que se entiendan y mensajes claros.
# - Dejo escrito qué significa True y qué significa False en cada caso.


# ==========================================
# Problem 1: Temperature converter and range flag
# ==========================================
# Description: Takes a temperature in Celsius and shows it in
# Fahrenheit and Kelvin. It also says if it is a high temperature
# (30 degrees or more).
#
# Inputs:
# - temp_c (float)
#
# Outputs:
# - "Fahrenheit: <temp_f>"
# - "Kelvin: <temp_k>"
# - "High temperature: True/False"
#
# Validations:
# - temp_c has to be a number
# - Kelvin cannot be below 0.0
#
# Test cases:
# 1) Normal: 25 -> Fahrenheit 77.0, Kelvin 298.15, High temperature False
# 2) Border: 30 -> Fahrenheit 86.0, Kelvin 303.15, High temperature True
# 3) Error: -300 -> error message and it asks again

# Ask for the temperature until it is a real number
while True:
    try:
        temp_c = float(input("Type the temperature in Celsius: "))
        temp_k = temp_c + 273.15

        # Nothing can be colder than 0 Kelvin, so those values are rejected
        if temp_k < 0.0:
            print("Error: temperature cannot be below absolute zero (0 Kelvin)")
            continue  # ask again

        # The number is fine, so we leave the loop
        break

    except ValueError:
        print("Error: invalid input")

# Convert to Fahrenheit and check if it is a hot day (30 or more)
temp_f = (temp_c * 9 / 5) + 32
is_high_temperature = (temp_c >= 30.0)

# Show the results
print(f"Fahrenheit: {temp_f}")
print(f"Kelvin: {temp_k}")
print(f"High temperature: {is_high_temperature}")


# ==========================================
# Problem 2: Work hours and overtime payment
# ==========================================
# Description: Calculates the weekly pay of a worker. Up to 40 hours
# are paid at the normal rate and the extra hours are paid 1.5 times.
# It also says if the worker had overtime.
#
# Inputs:
# - hours_worked (float)
# - hourly_rate (float)
#
# Outputs:
# - "Regular pay: <wage>"
# - "Overtime pay: <extra_wage>"
# - "Total pay: <total>"
# - "Has overtime: True/False"
#
# Validations:
# - hours_worked cannot be negative
# - hourly_rate has to be greater than 0
#
# Test cases:
# 1) Normal: 45 hours, rate 100 -> Regular 4000.0, Overtime 750.0,
#    Total 4750.0, Has overtime True
# 2) Border: 40 hours, rate 100 -> Regular 4000.0, Overtime 0.0,
#    Total 4000.0, Has overtime False
# 3) Error: -5 hours, rate 100 -> "Error: invalid input"

# Ask for the hours and the wage until both are numbers
while True:
    try:
        hours_worked = float(input("Type your total worked hours in the week: "))
        hourly_rate = float(input("Type your hourly wage: "))
        break
    except ValueError:
        print("Error: invalid input")

has_overtime = False

# Split the hours: up to 40 are regular, the rest are extra
regular_hours = min(hours_worked, 40)
overtime_hours = max(0, hours_worked - 40)

if hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input")
else:
    # Regular hours at the normal pay, extra hours at 1.5 times
    wage = hourly_rate * regular_hours
    extra_wage = overtime_hours * 1.5 * hourly_rate
    if hours_worked > 40:
        has_overtime = True

    print(f"Regular pay: {wage}")
    print(f"Overtime pay: {extra_wage}")
    print(f"Total pay: {extra_wage + wage}")
    print(f"Has overtime: {has_overtime}")


# ==========================================
# Problem 3: Discount eligibility with booleans
# ==========================================
# Description: Says if a customer gets a discount. They get 10% off if
# they are a student, a senior, or if the purchase is 1000 or more.
#
# Inputs:
# - purchase_total (float)
# - is_student_text (yes/no)
# - is_senior_text (yes/no)
#
# Outputs:
# - "Discount eligible: True/False"
# - "Final total: <final_total>"
#
# Validations:
# - purchase_total cannot be negative
# - The answers can only be yes or no
#
# Test cases:
# 1) Normal: 500, no, no -> Discount eligible False, Final total 500.00
# 2) Border: 1000, no, no -> Discount eligible True, Final total 900.00
# 3) Error: -50 -> "Error: invalid input" and it asks again

# Ask until the purchase and both answers make sense
while True:
    try:
        purchase_total = float(input("Type your total purchase: "))
        is_student_text = input("Are you a student? (yes/no): ").upper()
        is_senior_text = input("Are you a senior? (yes/no): ").upper()

        # The purchase cannot be negative
        if purchase_total < 0:
            print("Error: invalid input")
            continue

        # The answers can only be YES or NO
        if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
            print("Error: invalid input")
            continue

        break  # everything is fine, so we leave the loop

    except ValueError:
        print("Error: invalid input")

# Turn the yes/no answers into True/False
is_student = (is_student_text == "YES")
is_senior = (is_senior_text == "YES")

# Discount if they are a student, a senior or spent 1000 or more
discount_eligible = False
final_total = purchase_total

if is_student or is_senior or purchase_total >= 1000.0:
    discount_eligible = True
    final_total = purchase_total * 0.9

print(f"Discount eligible: {discount_eligible}")
print(f"Final total: {final_total:.2f}")


# ==========================================
# Problem 4: Basic statistics of three integers
# ==========================================
# Description: Takes three whole numbers and shows their sum, average,
# biggest, smallest, and if the three of them are even.
#
# Inputs:
# - n1, n2, n3 (int)
#
# Outputs:
# - "Sum: <sum_value>"
# - "Average: <average>"
# - "Max: <max_number>"
# - "Min: <min_number>"
# - "All even: True/False"
#
# Validations:
# - The three values have to be whole numbers (negatives are fine)
#
# Test cases:
# 1) Normal: 4, 7, 10 -> Sum 21, Average 7.00, Max 10, Min 4, All even False
# 2) Border: -2, 0, 4 -> Sum 2, Average 0.67, Max 4, Min -2, All even True
# 3) Error: "abc" -> "Error: invalid input"

try:
    n1 = int(input("Type a number: "))
    n2 = int(input("Type a number: "))
    n3 = int(input("Type a number: "))

    # Do the sum once and reuse it for the average
    sum_value = n1 + n2 + n3
    average = sum_value / 3
    max_number = max(n1, n2, n3)
    min_number = min(n1, n2, n3)

    # True only if the three numbers are even
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {average:.2f}")
    print(f"Max: {max_number}")
    print(f"Min: {min_number}")
    print(f"All even: {all_even}")
except ValueError:
    print("Error: invalid input")


# ==========================================
# Problem 5: Loan eligibility (income and debt ratio)
# ==========================================
# Description: Says if a person can get a loan. It looks at how much of
# the income goes to debts (debt ratio), the income itself and the
# credit score. All three conditions have to be met.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - "Debt ratio: <debt_ratio>"
# - "Eligible: True/False"
#
# Validations:
# - monthly_income has to be greater than 0 (we divide by it)
# - monthly_debt and credit_score cannot be negative
#
# Test cases:
# 1) Normal: 12000, 3000, 700 -> Debt ratio 0.25, Eligible True
# 2) Border: 8000, 3200, 650 -> Debt ratio 0.4, Eligible True
# 3) Error: 0, 500, 700 -> "Error: invalid input"

# Ask until the three data are numbers
while True:
    try:
        monthly_income = float(input("Type your monthly income: "))
        monthly_debt = float(input("Type your monthly debt payments: "))
        credit_score = int(input("Type your credit score: "))
        break
    except ValueError:
        print("Error: invalid input")

# Continue only if the numbers make sense (income cannot be 0)
if monthly_income > 0 and monthly_debt >= 0 and credit_score >= 0:
    # What part of the income goes to pay debts
    debt_ratio = monthly_debt / monthly_income

    # Eligible only if the three conditions are met
    eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

    print(f"Debt ratio: {debt_ratio}")
    print(f"Eligible: {eligible}")
else:
    print("Error: invalid input")


# ==========================================
# Problem 6: Body Mass Index (BMI) and category flag
# ==========================================
# Description: Calculates the BMI from weight and height and says if
# the person is underweight, normal or overweight. As an extra, it
# asks for gender (M/F) and age to estimate the body fat percentage.
#
# Inputs:
# - height_m (float)
# - weight_kg (float)
# - gender (M/F) and age (int) for the extra part
#
# Outputs:
# - "BMI: <bmi>"
# - "Your fat percentage is: <fat_percentage>%"
# - "Underweight: True/False"
# - "Normal: True/False"
# - "Overweight: True/False"
#
# Validations:
# - height_m and weight_kg have to be greater than 0
# - gender has to be M or F and age cannot be negative
#
# Test cases:
# 1) Normal: 1.70 m, 70 kg, M, 20 -> BMI 24.22, Normal True
# 2) Border: 2.0 m, 74 kg, M, 30 -> BMI 18.50, Normal True
#    (18.5 exactly already counts as normal)
# 3) Error: 1.70 m, 0 kg -> "Error: invalid input" and it asks again

# Ask for height and weight until they are numbers above 0
while True:
    try:
        height_m = float(input("Type your height in meters: "))
        weight_kg = float(input("Type your weight in kg: "))

        if weight_kg <= 0 or height_m <= 0:
            print("Error: invalid input")
            continue  # ask again if they are zero or negative

        break  # everything is fine, so we leave the loop

    except ValueError:
        print("Error: invalid input")

# BMI = weight divided by height squared
bmi = weight_kg / (height_m ** 2)
is_underweight = False
is_normal = False
is_overweight = False
print(f"BMI: {bmi:.2f}")

# Extra part: ask for gender and age (same idea, until they make sense)
while True:
    try:
        gender = input("Type your gender (M/F): ").lower()
        age = int(input("Type your age: "))

        if gender not in ("m", "f") or age < 0:
            print("Error: invalid input")
            continue

        break

    except ValueError:
        print("Error: invalid input")

# The formula changes a little for women and men
if gender == "f":
    fat_percentage = (1.20 * bmi + (0.23 * age) - 5.4)
else:
    fat_percentage = (1.20 * bmi + (0.23 * age) - 16.2)

print(f"Your fat percentage is: {fat_percentage:.2f}%")

# Check which group the BMI belongs to
if bmi < 18.5:
    is_underweight = True
elif 18.5 <= bmi < 25.0:
    is_normal = True
elif bmi >= 25:
    is_overweight = True

print(f"Underweight: {is_underweight}")
print(f"Normal: {is_normal}")
print(f"Overweight: {is_overweight}")


# ==========================================
# CONCLUSIONS
# ==========================================
# Casi todos los programas mezclan int y float: edades y puntajes
# enteros, sueldos y estaturas con decimales.
# Una comparación da True o False y con eso el if decide qué hacer.
# Con and tienen que cumplirse todas las condiciones, como en el
# préstamo, y con or basta una, como en el descuento.
# Revisar los datos antes de calcular evita resultados absurdos, y en
# el préstamo evita dividir entre cero. Este mismo patrón sirve en
# nómina, descuentos y créditos.

# ==========================================
# REFERENCES
# ==========================================
# 1) Python documentation - Built-in Types: Numeric Types (int, float)
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python documentation - Boolean Type (bool)
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python Tutorial - An Informal Introduction to Python (Numbers)
#    https://docs.python.org/3/tutorial/introduction.html#numbers
# 4) Python documentation - Boolean operations (and, or, not)
#    https://docs.python.org/3/reference/expressions.html#boolean-operations
# 5) Real Python - Numbers in Python
#    https://realpython.com/python-numbers/
# 6) W3Schools - Python Booleans
#    https://www.w3schools.com/python/python_booleans.asp
