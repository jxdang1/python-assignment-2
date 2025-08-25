# Header

print("*************************************")
print("* Jennifer Dang                     *")
print("* IS 826: Application Programming   *")
print("* Assignment 2: Compute Class Grade *")
print("* Date: 08/20/2025                  *")
print("*************************************\n")

print("""Purpose: This program calculates the average grade from
the user's entered grades and determines a letter grade to it.\n""")

# This stores the grades into a dictionary without making it a list or array

# This stores the grades into a dictionary without making it a list or array

def calculate_gradebook():
    student_grades = {}

    total_grade_sum = 0

    entered_grade_num = 0


# Loop that will ask User to enter a valid input 

while True:
    try:
        grade_input() = input("Enter the number of grades: ")

        if grade_input  == "":
            print("No input found.")
            return # Will exit function if no enter input was found
        
        entered_grade_num = int(grade_input)
        
        if entered_grade_num < 0:
            print("Number cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Invald input. Enter a whole number for number of grades.")

        if entered_grade_num == 0:
            print("Zero grades were entered.")
            return

# Condtional statement for final letter grade based on outcome of grade numbers


if class_average >= 90.0:
    letter_grade = "A"
elif class_average >= 80.0:
    letter_grade = "B"
elif class_average >= 70.0:
    letter_grade = "C"
elif class_average >= 60.0:
    letter_grade = "D"
else:
    letter_grade = "F"


print("The final letter grade is:", letter_grade)

calculate_gradebook():
