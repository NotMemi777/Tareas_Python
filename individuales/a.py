#7.1 Problem 1: Temperature converter and range flag
while True:
    try:
        temp_c = float(input("Type the temperature in Celcius: "))
        temp_k = temp_c + 273.15
        
        # Validar la restricción física (cero absoluto)
        if temp_k < 0.0:
            print("Error: La temperatura no puede estar por debajo del cero absoluto (0 Kelvin).")
            continue  # Vuelve al inicio del ciclo sin romperlo
            
        # Si la entrada es válida y físicamente posible, salimos del ciclo
        break
        
    except ValueError:
        print("Error: Por favor ingresa un número válido.")

# Operaciones de conversión y comparación
temp_f = (temp_c * 9 / 5) + 32
is_high_temperature = (temp_c >= 30.0)

# Salidas
print(f"Fahrenheit: <{temp_f}>")
print(f"Kelvin: <{temp_k}>")
print(f"High temperature: {is_high_temperature}")