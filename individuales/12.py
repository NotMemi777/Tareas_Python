#7.5 Problem 5: Password strength classifier

password = input ("Type your password: ")
clean_password = password.strip()
result = ""
has_upper = False
has_lower = False
has_digit = False
has_symbol = False

for caract in clean_password:
    if caract.isupper():
        has_upper = True
    elif caract.islower():
        has_lower = True
    elif caract.isdigit():
        has_digit = True
    elif not caract.isalnum():  # Ojo: si NO es alfanumérico, es símbolo
        has_symbol = True

if len(clean_password)>=8 and has_symbol and has_digit and has_lower and has_upper:
    result = "strong"
elif len(clean_password) >=8 and ((has_upper and has_lower) or has_digit):
        result = "medium"
else: result = "weak"
        
print (f"the password is: {result}")