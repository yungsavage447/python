# Variables and Data Types

student_name = "Ugwoke Kelechi"
student_age = 22
student_height = 1.75
is_registered = True

print(student_name, type(student_name))
print(student_age, type(student_age))
print(student_height, type(student_height))
print(is_registered, type(is_registered))








# Arithmetic Operations

student_age = 22
student_height = 2
print(student_age + student_height)
print(student_age - student_height)
print(student_age * student_height)
print(student_age / student_height)
print(student_age // student_height)
print(student_age % student_height)
print(student_age ** student_height)








# Comparison Operations

student_age = 22
minimum_age = 18

print(student_age == minimum_age)
print(student_age != minimum_age)
print(student_age > minimum_age)
print(student_age < minimum_age)
print(student_age >= minimum_age)
print(student_age <= minimum_age)








# Logical Operations

is_registered = True
has_paid_fees = True

print(is_registered and has_paid_fees)
print(is_registered or has_paid_fees)
print(not is_registered)









# Membership Operations

student_courses = ["Python", "HTML", "CSS", "JavaScript", "Database"]

selected_course = "Python"

print(selected_course in student_courses)

print(selected_course not in student_courses)








# Identity Operations

first_score = 85
second_score = 85

print(first_score is second_score)

print(first_score is not second_score)








# String Operations

first_name = "Ugwoke"
last_name = "Kelechi"

full_name = first_name + " " + last_name

print("Full Name:", full_name)








# String Formatting

student_name = "Ugwoke Kelechi"
student_age = 22
school_name = "University of Nigeria, Nsukka"
course = "Computer Science"
hobby = "Learning programming"
state_of_origin = "Enugu State"

student_bio = f"""
My name is {student_name}.
I am {student_age} years old.
I am a student of {school_name}.
I am studying {course}.
My hobby is {hobby}.
I am from {state_of_origin}.
I am passionate about technology and hope to become a professional software developer.
"""

print(student_bio)














# Student Information Program

# Creating student variables
student_name = "Ugwoke Kelechi"
student_age = 22
course = "Computer Science"

# Displaying student information
print("STUDENT INFORMATION")

print("Name:", student_name)
print("Age:", student_age)
print("Course:", course)

# Checking student's age
if student_age >= 18:
    print("The student is an adult.")
else:
    print("The student is not an adult.")
