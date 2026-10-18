#7.6 Problem 6: Product label formatter (fixed-width text)

product_name = input("Type the name of a product: ")
price_value = float(input("Type the price of the product: "))
clean_name = product_name.strip()

# Validaciones iniciales
if len(clean_name) == 0:
    print("Error: Product name cannot be empty.")
elif price_value <= 0:
    print("Error: A price cannot be 0 or less.")
else:
    # 1. Limitamos el nombre del producto primero para que nunca aplaste al precio
    # (Por ejemplo, un máximo de 11 caracteres para el nombre)
    clean_name = clean_name[:11]
    
    # 2. Armamos la etiqueta con el nombre seguro
    label = f"Product: {clean_name} | Price: ${price_value}"
    
    # 3. Como ahora la etiqueta mide menos de 30, la rellenamos con espacios al final
    label = label.ljust(30)
        
    # 4. Imprimimos el resultado final entre comillas
    print(f'Label: "{label}"')