#7.6 Problem 6: Simple contact book (dictionary CRUD)

contacts = {
    "Ängel (lord sixseven)": "8341676767",
    "Alan (FocaSlayer777)" : "8347776667",
    "Olaf (MachistMan)": "8346667749",
    "Mermilio(MrFeminist)": "8341806767"
}

print(contacts)

action_text = input("ADD, SEARCH or DELETE: ").upper()

if action_text == "ADD":
    name = input("Type a name: ")
    phone = input("Type the phone: ")
    contacts[name] = phone
    print(f"Contact saved: {name} {phone}")

elif action_text == "SEARCH":
    name = input("Type a contact to search: ")
    phone = contacts.get(name)
    if phone is not None:
        print(f"Phone: {phone}")
    else:
        print("Error: contact not found")

elif action_text == "DELETE":
    name = input("Type a contact to delete: ")
    deleted = contacts.pop(name, None)
    if deleted is not None:
        print(f"Contact deleted: {name}")
    else:
        print("Error: contact not found")