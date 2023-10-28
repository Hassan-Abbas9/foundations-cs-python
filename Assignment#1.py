#################################################################
#QUESTION-1
#ON hand answers are written on the right as a comment
print( 10* ( 90 + 2 )- 5)      # 915 - Correct
print( 10 * 90 + 2- 5 )        # 897 - Correct
print( 10 * 90+ ( 2- 5 ))      # 897 - Correct
print( 10.0 * ( 90 + 2 )-5)    # 915  - Correct but without .0
print( 120 / ( 20 + 40 ) -( 6 - 2)/ 4 )   # 1 - Correct but without .0
print( 5.0 / 2 )               # 2.5 - Correct
print( 5 / 2 )                 # 2.5 - Correct
print( 5.0 / 2.0 )             # 2.5 - Correct
print( 5 / 2.0 )               # 2.5 - Correct
print( 678 % 3 * ( 8 - ( 9 / 4 ))) # 0.0 - Correct

#################################################################
#QUESTION-2

id = int(input("Please enter the ID of the user: "))
name = input("Please enter the name of the user: ")
date_of_birth = input("Please enter the date of birth of the user: ")
address = input("please enter the address of the user: ")

print("Your profile - ID: 0", id, sep="")
print("Name: ", name.upper().strip())
print("DOB: ", date_of_birth)
print("Address: ", address.lower().strip())

#################################################################
#QUESTION-3

number = input("enter the number: ")
count = 0

for i in range(len(number)):
    count += 1

print(number, "has", count, "digits", sep=" ")

#################################################################
#QUESTION-4

percentage = int(input("Enter the grade of the student out of 100: "))

if percentage < 60:
    grade = 'F'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 60 and percentage < 63:
    grade = 'D-'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 63 and percentage < 67:
    grade = 'D'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 67 and percentage < 70:
    grade = 'D+'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 70 and percentage < 73:
    grade = 'C-'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 73 and percentage < 77:
    grade = 'C'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 77 and percentage < 80:
    grade = 'C+'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 80 and percentage < 83:
    grade = 'B-'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 83 and percentage < 87:
    grade = 'B'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 87 and percentage < 90:
    grade = 'B+'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 90 and percentage < 93:
    grade = 'A-'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 93 and percentage < 97:
    grade = 'A'
    print(percentage, "is equivalent to a ", grade)
elif percentage >= 97:
    grade = 'A+'
    print(percentage, "is equivalent to a ", grade)

#################################################################
#QUESTION-5

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    print('*' * i)

for i in range(n - 1, 0, -1):
    print('*' * i)

#################################################################
#QUESTION-6

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number: "))
i = first_number
even_numbers = []

while i <= second_number:
    if i % 2 == 0:
        even_numbers.append(i)
    i += 1

print(even_numbers)
