# Header

print("*************************************")
print("* Jennifer Dang                     *")
print("* IS 826: Application Programming   *")
print("* Assignment 2: Compute Class Grade *")
print("* Date: 08/20/2025                  *")
print("*************************************\n")

print("""Purpose: This program calculates the average grade from
the user's entered grades and determines a letter grade to it.\n""")


def calculate_gradebook():
    grade_sum = 0
    grade_count = 0

# Prompt user for how many numbers of grades that will be inputed

num_grades = input("Enter the number of grades: ")

# Validate input to ensure it's a positive integer
try:
    num_grades = int(num_grades_input)
    if num_grade <= 0:
        print("Please enter a positive integer.")
        return
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    return

amount_grades = int(num_grades)


for i in range(1, num_grades + 1):
    while True:
        try:
            #Use a dynamic variable to store the current grade
            start_grade = int(input(f"Enter grade #{i}: "))
            grade_sum += start_grade
            grade_count += 1
            break # Exit the inner loop on valid input
        except ValueError:
                print("Invalid input. Please enter an integer.")
                    


# Calculates the average

if grade_count > 0:
    average = grade_sum / grade_count
else:
    average = 0.0


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

calculate_gradebook()
