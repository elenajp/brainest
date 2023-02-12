age = 30
age2 = 12
# can't add 2 dif classes together
print("hello " + str(age + age2))
print("hello", age)

# kp framework?
# quotient
# % and //

x = 123456  # will print the last no, 6 in this case
reminder = x % 10
print(reminder)

# input by default is a string input() or you can do int(input()) or print it as an int
# docstrings - say what the function takes and what it returns

# 1
def welcome():
    """This function takes the users name as an imput and prints a greeting with their name"""
    name = input("Enter name: ")
    print("Hello, " + name + "!")


welcome()

# 2
def gross_pay():
    """A function that takes the hours and rate of a worker and prints the gross pay"""
    hours = int(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    print(hours * rate)


gross_pay()

# 3
def temperature_conversion():
    """A function that takes the celsius as an input and prints it as fahrenheit"""
    celsius = input("Enter the temp in celsius: ")
    print("fahrenheit = ", float(celsius) * 1.8 + 32)


temperature_conversion()

#####################################################################################

# boolean expressions e.g x == y, x !=y, x > y, etc

# "==" tests for value equality, meaning that it checks whether the two operands have the same value.
# "is" tests for object identity, meaning that it checks whether the two operands refer to the same object in memory.

# conditional statements if, elif, else

# # one liner
x = 5
print("x is pos") if x > 0 else print("x is not pos")

# x, y = 2, 3

## nested stuff
## error printing with try and except, try, except, else...if right then prints try and else. Can also use finnaly.
## raise an Exception is another error handling way

# Section 2
# 1


def employee_pay():
    """A function that takes the number of hours worked and returns the pay calculated with extra hours"""

    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if not type(hours) and type(rate) is not float:
        raise TypeError("only float allowed")

    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
        print(pay)
    else:
        pay = hours * rate
        print(pay)


employee_pay()

# Section 2
# 2
def score():
    """A function that takes a score as input and prints an error message if it is out of range or prints a grade if in range"""
    score = float(input("Enter score: "))

    if score < 0.0 or score > 1.0:
        print("Error: score is out of range")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")


score()
