#7.4 Problem 4: Sentence word stats (lengths and first/last word)

message = input("Type a sentence: ")
without_spaces = message.strip()
separating_message = without_spaces.split()

# 1. Validar que la lista tenga al menos una palabra
if len(separating_message) > 0:
    word_count = len(separating_message)
    short = separating_message[0]
    large = separating_message[0]

    # 2. El bucle DEBE ir dentro del if
    for word in separating_message:
        if len(word) < len(short):
            short = word
        if len(word) > len(large):
            large = word

    # 3. Las impresiones con el formato exacto requerido
    print(f"Word count: {word_count}")
    print(f"First word: {separating_message[0]}")
    print(f"Last word: {separating_message[-1]}")
    print(f"Shortest word: {short}")
    print(f"Longest word: {large}")

else:
    print("Error: The sentence cannot be empty.")