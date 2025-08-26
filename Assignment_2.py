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

    # Prompt the user for the number of grades to input.
    num_grades_input = input("Enter the number of grades: ")

    # Validate input to ensure it's a positive integer and creates a try except block that handles cases where numbers aren't inputed
    try:
        num_grades = int(num_grades_input)
        if num_grades <= 0:
            print("Invalid input. Please enter a positive integer.")
            return # Exit the function if the number is not positive.
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return # Exit the function on non-integer input.

   # Loop to get each grade from the user.

    for i in range(num_grades):
        while True:
            try:
                # The f-string helps formats the prompt to show the number of grade entered
                current_grade = int(input(f"Enter grade #{i + 1}: "))
                
                # Check if the grade is within a valid range
                if 0 <= current_grade <= 100:
                    grade_sum += current_grade
                    grade_count += 1
                    break # Exit the loop if valid range is entered
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Please enter an integer.")


    # Calculates the average
    
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


    print(f"\nAverage grade: {grade_average:.2f}") # Format to 2 decimal places.
    print(f"The final letter grade is: {letter_grade}")

# Calls function
calculate_gradebook()
