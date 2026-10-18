# 7.3 Problem 3: Discount eligibility with booleans

while True:
    try:
        purchase_total = float(input("Type your total purchase: "))
        is_student_text = input("You are a student? (yes/no): ").upper()
        is_senior_text = input("You are a senior? (yes/no): ").upper()
        
        # Validación: La compra no puede ser negativa
        if purchase_total < 0:
            print("Error: invalid input")
            continue
            
        # Validación: El texto debe ser exclusivamente YES o NO
        if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
            print("Error: invalid input")
            continue
            
        break # Si todo es correcto, rompemos el ciclo y avanzamos
        
    except ValueError:
        print("Error: invalid input")

# Lógica del descuento
discount_eligible = False
final_total = purchase_total

if is_student_text == "YES" or is_senior_text == "YES" or purchase_total >= 1000:
    discount_eligible = True
    final_total = purchase_total * 0.9

# Salidas requeridas
print(f"Discount eligible: {discount_eligible}")
print(f"Final Total: {final_total:.2f}")