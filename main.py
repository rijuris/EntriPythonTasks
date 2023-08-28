#Exercise 3
number1= int (input("First number:"))
number2= int (input("Second number:"))
sum=number1+number2
multi=number1*number2
sub=number1-number2
div=number1/number2
perc = number1%number2

print("Two numbers are:", number1,',',number2)
print(number1, "+", number2, "=", sum)
print(number1, "-", number2, "=", sub)
print(number1, "/", number2, "=", div)
print(number1, "X", number2, "=", multi)
print(number1, "%", number2, "=", perc)

# Write a program that reads an integer value from the user and prints output whether it is odd or even.
# An example run of the program (numbers in bold are typed in by the user)
# Enter a number: 13
# 13 is “even”
number = int(input("Enter your number: "))
if number % 2 ==0:
    print(number, 'is "odd"')
else:
    print(number, 'is "even"')

#Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
#An example run of the program
#Enter the month: 3
#Month 3 is March

month = int(input("Enter the month: "))
if month == 1:
    print ("Month", month, "is January")
elif month == 2:
    print ("Month", month, "is february")
elif month ==3:
    print ("Month", month, "is March")
elif month ==4:
    print("Month", month, "is April")
elif month ==5:
    print("Month", month, "is May")
elif month ==6:
    print ("Month", month, "is June" )
elif month ==7:
    print ("Month", month, "is July")
elif month ==8:
    print ("Month", month, "is August")
elif month ==9:
    print("Month", month, "is September")
elif month ==10:
    print ("Month", month, "is October")
elif month ==11:
    print ("Month", month, "is November")
elif month ==12:
    print ("Month", month, "is December")
if month >= 13:
    print ("Oops only 12 months are there in a year")

#Create a function that takes in three arguments, two of which are optional. The first argument
#should be a required positional argument, the second argument should be a keyword argument
#with a default value of 10, and the third argument should be a keyword argument with a default
#value of None. The function should print the sum of the first two arguments if the third argument
#is None, and print the product of all three arguments if the third argument is not None.

def custom_function(arg1, arg2=10, arg3=None):
    if arg3 is None:
        result = arg1 + arg2
    else:
        result = arg1 * arg2 * arg3
    print(f"Result: {result}")

# Example usage:
custom_function(5)          # Result: 15 (arg1 + arg2)
custom_function(5, 2)       # Result: 7 (arg1 + arg2)
custom_function(5, 2, 3)    # Result: 30 (arg1 * arg2 * arg3)

#Create a function that takes in an arbitrary number of arguments and prints the sum of all the
#even numbers. If no even numbers are provided, the function should print 0.

def sum_even_numbers(*args):
    even_sum = 0
    for num in args:
        if isinstance(num, int) and num % 2 == 0:
            even_sum += num
    print(f"Sum of even numbers: {even_sum}")

# Example usage:
sum_even_numbers(2, 4, 6, 8)       # Sum of even numbers: 20
sum_even_numbers(1, 3, 5, 7)       # Sum of even numbers: 0 (no even numbers provided)
sum_even_numbers(10, 15, 20, 25)   # Sum of even numbers: 30

#Create a function that takes in two required arguments, one optional keyword argument with a
#default value of 1, and one arbitrary argument. The function should print the product of the two
#required arguments, multiplied by the optional keyword argument, multiplied by the product of all
#the values in the arbitrary argument.

def custom_function(arg1, arg2, arg3=1, *args):
    result = arg1 * arg2 * arg3

    for num in args:
        result *= num

    print(f"Result: {result}")

# Example usage:
custom_function(2, 3, 4)  # Result: 24 (2 * 3 * 4)
custom_function(2, 3, 4, 5)  # Result: 120 (2 * 3 * 4 * 5)
custom_function(2, 3, 4, 5, 6)  # Result: 720 (2 * 3 * 4 * 5 * 6)
custom_function(2, 3, arg3=4)  # Result: 24 (2 * 3 * 4)
custom_function(2, 3, 4, 5, 6, 7, 8)  # Result: 20160 (2 * 3 * 4 * 5 * 6 * 7 * 8)

#Write a function that takes in a list of strings and returns a new list with only the strings that have
#a length greater than or equal to 5.
def filter_strings_by_length(strings):
    filtered_strings = [s for s in strings if len(s) >= 5]
    return filtered_strings

# Example usage:
input_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
result = filter_strings_by_length(input_list)
print(result)  # Output: ["apple", "banana", "cherry", "elderberry"]

#Write a function that takes in a list of strings and returns a new list with all the vowels removed.

def remove_vowels(strings):
    vowels = "AEIOUaeiou"  # Define a string containing all vowels

    # Use a list comprehension to remove vowels from each string
    result = [''.join(char for char in s if char not in vowels) for s in strings]

    return result


# Example usage:
input_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
result = remove_vowels(input_list)
print(result)
# Output: ['ppl', 'bnna', 'chrry', 'dt', 'ldrberry', 'fg']

#Topic : Recursion, lambda, eval and filter

#Write a Python program to calculate the sum of a list of numbers using recursion
def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        # The sum of the first element and the sum of the rest of the list
        return numbers[0] + recursive_sum(numbers[1:])

# Example usage:
numbers_list = [1, 2, 3, 4, 5]
result = recursive_sum(numbers_list)
print(f"The sum of {numbers_list} is {result}")
# Output: The sum of [1, 2, 3, 4, 5] is 15

#Topic : Recursion, lambda, eval and filter
# Exercise 1: Calculate the Sum of a List of Numbers Using Recursion

def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])

numbers_list = [1, 2, 3, 4, 5]
result = recursive_sum(numbers_list)
print(f"The sum of {numbers_list} is {result}")


# Exercise 2: Lambda Function to Check Even

is_even = lambda x: x % 2 == 0

# Example usage:
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False


# Exercise 3: Lambda Functions for Addition and Multiplication

add_15 = lambda x: x + 15
multiply = lambda x, y: x * y

# Example usage:
print(add_15(10))          # Output: 25
print(multiply(5, 6))      # Output: 30


# Exercise 4: Evaluate a Mathematical Expression using eval()

expression = "3 * 5 + 2"
result = eval(expression)
print(f"The result of the expression '{expression}' is {result}")


# Exercise 5: Evaluate a Logical Expression using eval()

expression = "5 > 2 and 3 < 4"
result = eval(expression)
print(f"The result of the expression '{expression}' is {result}")


# Exercise 6: Evaluate a Python Expression using eval()

expression = "[x * 2 for x in range(5)]"
result = eval(expression)
print(f"The result of the expression '{expression}' is {result}")


# Exercise 7: Filter Out Vowels from a List of Characters using filter()

def is_vowel(char):
    return char.lower() not in 'aeiou'

characters = ['a', 'b', 'c', 'd', 'e', 'f']
filtered_characters = list(filter(is_vowel, characters))
print(f"Filtered characters: {filtered_characters}")


# Exercise 8: Filter Out Prime Numbers using filter()

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(is_prime, numbers))
print(f"Prime numbers: {prime_numbers}")


# Exercise 9: Filter Strings with Length > 5 using filter()

def long_strings(s):
    return len(s) > 5

strings = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
filtered_strings = list(filter(long_strings, strings))
print(f"Filtered strings: {filtered_strings}")

#Topic : map, reduce, generators and decorators
# Exercise 1: Convert a List of Strings to Uppercase using map()

string_list = ["hello", "world", "python"]
uppercase_list = list(map(lambda x: x.upper(), string_list))
print(uppercase_list)


# Exercise 2: Square Each Number in a List using map()

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)


# Exercise 3: Calculate the Length of Each String in a List using map()

strings = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
lengths = list(map(lambda x: len(x), strings))
print(lengths)


# Exercise 4: Calculate the Sum of Elements in a List using reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"The sum of {numbers} is {sum_result}")


# Exercise 5: Calculate the Product of Elements in a List using reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product_result = reduce(lambda x, y: x * y, numbers)
print(f"The product of {numbers} is {product_result}")


# Exercise 6: Find the Maximum Element in a List using reduce()

from functools import reduce

numbers = [3, 9, 1, 7, 5]
max_result = reduce(lambda x, y: x if x > y else y, numbers)
print(f"The maximum element in {numbers} is {max_result}")


# Exercise 7: Generator Function to Yield Words in a String

def words_generator(text):
    words = text.split()
    for word in words:
        yield word

text = "This is a sample sentence."
word_gen = words_generator(text)
for word in word_gen:
    print(word)


# Exercise 8: Generator Function to Yield Even Numbers from a List

def even_numbers_generator(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_gen = even_numbers_generator(numbers)
for num in even_gen:
    print(num)


# Exercise 9: Generator Function to Yield Strings Starting with a Vowel

def vowel_start_generator(strings):
    vowels = 'AEIOUaeiou'
    for s in strings:
        if s[0] in vowels:
            yield s

strings = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
vowel_start_gen = vowel_start_generator(strings)
for s in vowel_start_gen:
    print(s)

#Topic : File handling
# Exercise 1: Read and Display the Contents of a File

# Assuming there's a file named 'sample.txt' with content
# "Hello, this is a sample file."

with open('sample.txt', 'r') as file:
    file_contents = file.read()
    print(file_contents)


# Exercise 2: Count the Number of Lines in a File

# Assuming there's a file named 'sample.txt' with multiple lines of text.

with open('sample.txt', 'r') as file:
    line_count = sum(1 for line in file)
    print(f"Number of lines in 'sample.txt': {line_count}")


# Exercise 3: Write Text to a File

# Create a new file 'output.txt' and write text to it.

with open('output.txt', 'w') as file:
    file.write("This is some text that has been written to 'output.txt'.")


# Exercise 4: Append Text to a File

# Append additional text to the existing 'output.txt' file.

with open('output.txt', 'a') as file:
    file.write("\nThis text is appended to 'output.txt'.")


# Exercise 5: Copy the Contents of One File to Another

# Copy the contents of 'source.txt' to 'destination.txt'.

with open('source.txt', 'r') as source_file:
    with open('destination.txt', 'w') as dest_file:
        dest_file.write(source_file.read())


# Exercise 6: Count the Total Number of Words in a File

# Assuming there's a file named 'sample.txt' with multiple words.

with open('sample.txt', 'r') as file:
    text = file.read()
    words = text.split()
    word_count = len(words)
    print(f"Total number of words in 'sample.txt': {word_count}")


# Exercise 7: Count the Occurrences of a Specific Word in a File

# Assuming there's a file named 'sample.txt' with text.

word_to_count = "sample"
with open('sample.txt', 'r') as file:
    text = file.read()
    word_count = text.lower().count(word_to_count.lower())
    print(f"The word '{word_to_count}' appears {word_count} times in 'sample.txt'")


# Exercise 8: Count the Number of Unique Words in a File

# Assuming there's a file named 'sample.txt' with text.

with open('sample.txt', 'r') as file:
    text = file.read()
    words = text.split()
    unique_words = set(words)
    unique_word_count = len(unique_words)
    print(f"Number of unique words in 'sample.txt': {unique_word_count}")

#Topic : Exception Handling
# Exercise 1: Convert String to Integer with Exception Handling

try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"Successfully converted to integer: {number}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


# Exercise 2: Raise an Exception for Negative Integers in a List

numbers = [1, 2, -3, 4, -5]
try:
    for num in numbers:
        if num < 0:
            raise ValueError("Negative integers are not allowed.")
except ValueError as e:
    print(e)


# Exercise 3: Calculate Average with Exception Handling

try:
    num_list = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
    average = sum(num_list) / len(num_list)
    print(f"The average of the numbers is: {average}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot calculate average of an empty list.")
finally:
    print("Program has finished running.")


# Exercise 4: Write Text to a File with Exception Handling

try:
    with open('output.txt', 'w') as file:
        file.write("This is some text that has been written to 'output.txt'.")
    print("Text written to 'output.txt'.")
except IOError as e:
    print(f"An error occurred: {e}")


# Exercise 5: Handle File Not Found Exception

try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")


# Exercise 6: Handle Division by Zero Exception

try:
    num = 5 / 0
    print(num)
except ZeroDivisionError:
    print("Division by zero is not allowed.")


# Exercise 7: Handle IndexError Exception

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Index out of range.")


# Exercise 8: Handle NameError Exception

try:
    print(undefined_variable)
except NameError:
    print("Variable is not defined.")


# Exercise 9: Handle Multiple Exceptions

try:
    result = 10 / 0
    print(result)
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")

#Topic : object oriented programming
# Exercise 1: Course Catalog with Base and Subclasses

class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type


# Exercise 2: Shape Class with Rectangle Subclass

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Exercise 3: Vehicle Class with Car and Motorcycle Subclasses

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

#Topic : Modules and RegEx

# Exercise 1: Calculate Square Root using math module

import math

number = 16
square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root}")


# Exercise 2: Generate a Random Number using random module

import random

random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")


# Exercise 3: Convert String to Uppercase using string module

import string

text = "hello world"
uppercase_text = text.upper()
print(f"Uppercase text: {uppercase_text}")


# Exercise 4: Calculate Factorial using math module

import math

number = 5
factorial = math.factorial(number)
print(f"The factorial of {number} is {factorial}")


# Exercise 5: Calculator Module for Arithmetic Operations

# Calculator module saved as "calculator.py"
# Example usage:
from calculator import add, subtract, multiply, divide

result = add(10, 5)
print(f"Addition: {result}")

result = subtract(10, 5)
print(f"Subtraction: {result}")

result = multiply(10, 5)
print(f"Multiplication: {result}")

result = divide(10, 5)
print(f"Division: {result}")


# Exercise 6: Greetings Module for Different Languages

# Greetings module saved as "greetings.py"
# Example usage:
from greetings import greet_english, greet_spanish, greet_french

print(greet_english())
print(greet_spanish())
print(greet_french())


# Exercise 7: Employee Module with Class and Methods

# Employee module saved as "employee.py"
# Example usage:
from employee import Employee

employee = Employee("John", 50000)
print(f"Employee Name: {employee.get_name()}")
print(f"Employee Salary: ${employee.get_salary()}")


# Exercise 8: Math Operations Module for Area Calculations

# Math Operations module saved as "math_operations.py"
# Example usage:
from math_operations import calculate_circle_area, calculate_rectangle_area, calculate_triangle_area

circle_area = calculate_circle_area(5)
print(f"Circle Area: {circle_area} square units")

rectangle_area = calculate_rectangle_area(4, 6)
print(f"Rectangle Area: {rectangle_area} square units")

triangle_area = calculate_triangle_area(3, 4)
print(f"Triangle Area: {triangle_area} square units")


# Exercise 9: File Operations Module for Reading and Writing Text Files

# File Operations module saved as "file_operations.py"
# Example usage:
from file_operations import read_file, write_file

text = read_file("sample.txt")
write_file("output.txt", text)


# Exercise 10: Temperature Conversion Module

# Temperature Conversion module saved as "temperature_conversion.py"
# Example usage:
from temperature_conversion import celsius_to_fahrenheit, fahrenheit_to_celsius

celsius = 20
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")

fahrenheit = 68
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is {celsius}°C")

import re  # Import the regular expressions module

# Given text for exercises 13 to 19
text = '''The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog again.
The quick brown cat jumps over the lazy dog.'''

# Exercise 11: Regular Expression to Match a Valid Phone Number (XXX-XXX-XXXX)

phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(f"Valid phone numbers: {phone_numbers}")


# Exercise 12: Regular Expression to Match a Valid Date (MM/DD/YYYY)

dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)
print(f"Valid dates: {dates}")


# Exercise 13: Regular Expression to Find All Occurrences of "fox"

occurrences_fox = re.findall(r'fox', text)
print(f"Occurrences of 'fox': {occurrences_fox}")


# Exercise 14: Regular Expression to Find All Occurrences of "quick"

occurrences_quick = re.findall(r'quick', text)
print(f"Occurrences of 'quick': {occurrences_quick}")


# Exercise 15: Regular Expression to Find Words Starting with "c"

words_starting_with_c = re.findall(r'\b[cC]\w+', text)
print(f"Words starting with 'c': {words_starting_with_c}")


# Exercise 16: Regular Expression to Find "lazy" Followed by Any One Character

lazy_followed_by_one_char = re.findall(r'lazy.', text)
print(f"'lazy' followed by one character: {lazy_followed_by_one_char}")


# Exercise 17: Use match() to Find if the Text Starts with "The"

starts_with_the = re.match(r'The', text)
if starts_with_the:
    print("Text starts with 'The'")
else:
    print("Text does not start with 'The'")


# Exercise 18: Use search() to Find the First Occurrence of "fox"

first_occurrence_fox = re.search(r'fox', text)
if first_occurrence_fox:
    print(f"First occurrence of 'fox': {first_occurrence_fox.group()}")


# Exercise 19: Use search() to Find First Occurrences Starting with "c"

first_occurrences_starting_with_c = re.search(r'\b[cC]\w+', text)
if first_occurrences_starting_with_c:
    print(f"First word starting with 'c': {first_occurrences_starting_with_c.group()}")



