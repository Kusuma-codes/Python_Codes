student_marks = (87, 92, 76, 88, 95, 68, 79, 85, 91, 73)

print("1. Show All Marks")
print("2. Find Highest Mark")
print("3. Find Lowest Mark")
print("4. Calculate Average")
print("5. Count How Many Got Above 80")
print("6. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("All Marks:", student_marks)

elif choice == 2:
    print("Highest Mark:", max(student_marks))

elif choice == 3:
    print("Lowest Mark:", min(student_marks))

elif choice == 4:
    average = sum(student_marks) / len(student_marks)
    print("Average Mark:", round(average, 2))

elif choice == 5:
    above_80 = sum(1 for mark in student_marks if mark > 80)
    print(f"Number of students who scored above 80: {above_80}")

elif choice == 6:
    print("Exiting...")

else:
    print("Invalid choice. Please select a valid option.")
