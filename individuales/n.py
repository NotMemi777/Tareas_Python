#7.2 Problem 2: Points and distances with tuples

while True: 
    try:
        x1 = float(input("Type coords x1: "))
        y1 = float(input("Type coords y1: "))
        x2 = float(input("Type coords x2: "))
        y2 = float(input("Type coords y2: "))
        
        point_a = (x1, y1)
        point_b = (x2, y2)
        
        # La raíz cuadrada ( ** 0.5 ) debe abarcar toda la suma de los cuadrados
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        middle_point = ((x1 + x2) / 2, (y1 + y2) / 2)
        
        print(f"Point A: {point_a}")
        print(f"Point B: {point_b}")
        print(f"Distance: {distance}")
        print(f"Midpoint: {middle_point}")
        
        break  # Rompe el ciclo porque todo salió bien
        
    except ValueError: 
        print("Please type a valid value")