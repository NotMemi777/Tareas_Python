#7.4 Problem 4: Student grades with dict and list

grades = { 
    "Alan" : [67, 80, 100],
    "Víctor": [90, 100, 67],
    "Olaf" : [100, 100, 67]
}
print(grades)

while True:
    try: 
        student_name = input("Type a name of a student: ").strip()
        
        if student_name in grades: 
            average = sum(grades[student_name]) / len(grades[student_name])
            
            is_passed = False
            if average >= 70.0:
                is_passed = True
                
            print(f"Grades: {grades[student_name]}")
            print(f"Average: {average}")
            print(f"Passed: {is_passed}")
        else:
            print("Error: student not found")
            
    except ValueError:
        print("Please type a valid value")

