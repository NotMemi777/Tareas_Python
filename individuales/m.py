# 7.1 Problem 1: Shopping list basics (list operations)

# 1. Pedir la lista inicial y dividirla por comas
initial_items_text = input("Add items to your list: ").split(",")
clean_items_list = []

# 2. Ciclar para limpiar los espacios de cada elemento inicial y agregarlos a la lista limpia
for item in initial_items_text: 
    clean_item = item.strip()
    clean_items_list.append(clean_item)

# 3. Pedir el nuevo producto y agregarlo directamente a la lista limpia
new_item = input("Add a new item: ")
clean_items_list.append(new_item)

# 4. Pedir el producto a buscar
search_item = input("Type an item that you want to search: ")

# 5. Validar que las entradas no estén vacías antes de procesar resultados
if len(new_item) > 0 and len(search_item) > 0:
    # Calcular resultados con la lista ya completa
    total_items = len(clean_items_list)
    is_in = search_item in clean_items_list
    
    # Imprimir los resultados
    print(f"Items list: {clean_items_list}")
    print(f"Total items: {total_items}")
    print(f"Found item: {is_in}")
else: 
    print("Please add an item or search one")

