# ==========================================
# Problem 1: Full Name Formatter (Name + Initials)
# ==========================================

# Prompt the user for their name and remove leading/trailing spaces
full_name = input("Name: ").strip()

# Split the input string into a list of words based on whitespace
words = full_name.split()

# Validate that the input is not empty and contains at least two words (first name + last name)
if not full_name or len(words) < 2:
    print("Type at least a name and full name")
else: 
    # Reconstruct the name with a single space between words
    clean_name = " ".join(words)
    
    # Capitalize the first letter of each word
    formatted_name = clean_name.title()
    
    # Extract the first letter of each word, convert to uppercase, join with dots, and append a trailing dot
    initials = ".".join([word[0].upper() for word in words]) + "."
    
    # Output the formatted full name and its initials
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# ==========================================
# Problem 2: Simple Email Validator (Structure + Domain)
# ==========================================

# Prompt for email input and remove outer whitespace
email_text = input("email: ").strip()

# Find the index of the '@' symbol
at_position = email_text.find("@")

# Extract the substring after the '@' symbol (the domain part)
domain_part = email_text[at_position + 1:]

# Evaluate all validation rules:
# 1. Ensure input is not empty
# 2. Check for no inner spaces
# 3. Ensure exactly one '@' character exists
# 4. Verify that the domain part contains at least one dot '.'
is_valid = (
    len(email_text) > 0 and 
    " " not in email_text and 
    email_text.count("@") == 1 and 
    "." in domain_part
)

# Output validation results according to specifications
if is_valid: 
    print("Valid email: true")
    print(f"Domain: {domain_part}")
else: 
    print("Valid email: false")


# ==========================================
# Problem 3: Palindrome Checker (Ignoring Spaces and Case)
# ==========================================

# Prompt for a phrase and convert all characters to lowercase
palindrome = input("Checking if it is a palindrome: ").lower()

# Remove all spaces between words to normalize the string
clean_pal = palindrome.replace(" ", "")

# Validate that the normalized string has a minimum length of 3 characters
is_valid = len(clean_pal) >= 3

# Reverse the normalized string using slicing
checking_pal = clean_pal[::-1]

# Check if the normalized string equals its reverse AND meets the length requirement
if clean_pal == checking_pal and is_valid: 
    print("Is palindrome: true")
    print(clean_pal)
else:
    print("Is palindrome: false")
    
    