# Header

print("*************************************")
print("* Jennifer Dang                     *")
print("* IS 826: Application Programming   *")
print("* Assignment 2: Compute Class Grade *")
print("* Date: 08/26/2025                  *")
print("*************************************\n")

print("""Purpose: This program calculates the average grade from
the user's entered grades and determines a letter grade to it.\n""")


def calculate_gradebook():

    grade_sum = 0
    grade_count = 0
    grades_list = []

    # User is prompted to enter the number of grades 

    num_grades_input = input("Enter the number of grades: ")
    num_grades = int(num_grades_input)

    # Loop to get each grade from the user.
    for i in range(num_grades):
        current_grade = int(input(f"Enter grade {i + 1}: "))
        
        # Check if the grade is within a valid range.
        if 0 <= current_grade <= 100:
            grade_sum += current_grade
            grade_count += 1
            grades_list = grades_list + [current_grade]
        else:
            print("Please enter a grade between 0 and 100.")

    # Header and dashes to mimic similar layout of assignment

    print(f"\n{'PYTHON GRADEBOOK':^80}")
    print(f"{'-----------------------':^80}")


   # create for loop that inputs the grades that was previously entered to be displayed
    i = 1
    for grade in grades_list:
        print(f"       Grade {i}: {grade:>6.1f}".center(70))
        i += 1
    
    print(f"{'-----------------------':^80}")

    # Calculates the average.
    if grade_count > 0:
        grade_average = grade_sum / grade_count
    else:
        grade_average = 0.0

    # Conditional statement for final letter grade from the calculated average
    
    if grade_average >= 90.0:
        letter_grade = "A"
    elif grade_average >= 80.0:
        letter_grade = "B"
    elif grade_average >= 70.0:
        letter_grade = "C"
    elif grade_average >= 60.0:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Print the final average and letter grade.
    print(f"The class average is: {grade_average:.2f}".center(80)) # Format to 2 decimal places.
    print(f"The final letter grade is: {letter_grade}".center(80))
    
# Call the function to run the program.
calculate_gradebook()
