##############################
# QUESTION - 1
##############################

def string_reverse(s, i):
    if i == 0:
        return ""
    else:
        return s[::-1] * i


s = input("Enter a string: ")
i = int(input("Enter the number of repetitions: "))
print(string_reverse(s, i))


##############################
# QUESTION - 2
##############################

def string_capitals_first(s):
    upper = ""
    lower = ""
    for i in range(len(s)):
        if s[i].isupper():
            upper = upper + s[i]
        elif s[i].islower():
            lower = lower + s[i]
    return upper + lower


s = input("Enter a string: ")
print(string_capitals_first(s))


##############################
# QUESTION - 3
##############################

def string_reordered(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    return sorted(s1) == sorted(s2)


s1 = input("Enter the string 1: ")
s2 = input("Enter the string 2: ")
print(string_reordered(s1, s2))


##############################
# Question - 4
##############################

def max_number(lst):
    max_no = lst[0]
    max_index = -1
    for i in range(1, len(lst)):
        element = lst[i]
        if element > max_no:
            max_no = element
            max_index = i
    return max_index, max_no


input_str = input("Enter the numbers seperated by spaces: ")
lst = [int(num) for num in input_str.split()]
index, max_no = max_number(lst)
print(f'Maximum number is: {max_no} at index: {index}')


# ##############################
# # Question - 5
# ##############################

def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        remainder = num % 10
        num = num // 10
        return remainder + sum_of_digits(num)


num = int(input("Enter the number: "))
print(f'The sum of digits {num} is {sum_of_digits(num)}')


# ##############################
# # Question - 6
# ##############################

def remove_duplicates(string):
    if not string:
        return ""

    new_string = string[0]
    for i in range(1, len(string)):

        if string[i].lower() != string[i - 1].lower():
            new_string = new_string + string[i]


s = input("Enter a string: ")
print(remove_duplicates(s))


# ##############################
# # Question - 7
# ##############################

def reverse_number(num):
    if num == 0:
        return "0"
    else:
        last_digit = num % 10
        num = num // 10
        return str(last_digit) + str(reverse_number(num))


number = int(input("Enter the number: "))
print("The reversed number of ", number, "is: ", reverse_number(number))
