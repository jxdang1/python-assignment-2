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


    # Validate input to ensure it's a positive integer and creates a try except block that handles cases where numbers aren't inputed
    while True:
        try:
            # Code that you want to run at least once
            current_grade = int(input(f"Enter grade {i + 1}: "))
            
            # Condition to check
            if 0 <= current_grade <= 100:
                # If the condition is met, break the loop
                break
            else:
                print("Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

   # Loop to get each grade from the user.

    for i in range(num_grades_input):
        while True:
            try:
                # The f-string helps formats the prompt to show the number of grade entered
                current_grade = int(input(f"Enter grade #{i + 1}: "))
                
                # Check if the grade is within a valid range
                if 0 <= current_grade <= 100:
                    grade_sum += current_grade
                    grade_count += 1
                    grades_list.append(current_grade)
                    break # Exit the loop if valid range is entered
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Please enter an integer.")


    
    # Header and dashes to mimic similar layout of assignment
    print(f"\n{'PYTHON GRADEBOOK':^80}")
    print(f"{'-----------------------':^80}")


    # enumerate() is used to give counter along with each grade when using a for loop
    
    for i, grade in enumerate(grades_list):
        # Mimic layout of assignment
        print(f"       Grade {i + 1:}: {grade:.2f}".center(70))

    print(f"{'-----------------------':^80}")


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

        print(f"The class average is: {grade_average:.2f}".center(80)) # Format to 2 decimal places.
    print(f"The final letter grade is: {letter_grade}".center(80))
    
# Calls function
calculate_gradebook()

