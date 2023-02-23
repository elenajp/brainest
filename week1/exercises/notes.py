# def my_function(x):
#     return 5 * x

# print(my_function(3))


# def computepay(hours, rate):
#     """Takes in the hours worked and the rate paid. Then returns the total pay after working overtime."""
#     if hours > 40:
#         regular_pay = 40 * rate
#         overtime_pay = (hours - 40) * (rate * 1.5)
#         pay = regular_pay + overtime_pay
#         return pay


# print(computepay(45, 10))

###############################################
# def computegrade(score):
#     try:
#         score_float = float(score)
#         if isinstance(score_float, float):
#             # if isinstance(score, float):
#             if score >= 0.9:
#                 print("Your grade is A")
#             elif score >= 0.8:
#                 print("Your grade is B")
#             elif score >= 0.7:
#                 print("Your grade is C")
#             elif score >= 0.6:
#                 print("Your grade is D")
#             else:
#                 print("Your grade is E")
#     except ValueError:
#         print("Please enter a float")


# computegrade(score=input("Enter your score: "))
###############################################

# problem
# print("Good morning!")
# print("How are you feeling?")
# feeling = input()
# print("I am happy to hear that you are feeling " + feeling + ".")
# print("Good afternoon!")
# print("How are you feeling?")
# feeling = input()
# print("I am happy to hear that you are feeling " + feeling + ".")
# print("Good evening!")
# print("How are you feeling?")
# feeling = input()
# print("I am happy to hear that you are feeling " + feeling + ".")


# def greeting():
#     times = ["morning", "afternoon", "evening"]
#     for time in times:
#         print(f"Good {time}!")
#         print("How are you feeling?")
#         feeling = input("Enter how you are feeling: ")
#         print(f"I am happy to hear that you are feeling {feeling}.")


# greeting()


# # solution 1
# def askFeeling():
#     print('How are you feeling?')
#     feeling = input()
#     print('I am happy to hear that you are feeling ' + feeling + '.')
#     print('Good morning!')
#     askFeeling()
#     print('Good afternoon!')
#     askFeeling()
#     print('Good evening!')
#     askFeeling()
#     for timeOfDay in ['morning', 'afternoon', 'evening']:
#         print('Good ' + timeOfDay + '!')
#         print('How are you feeling?')
#         feeling = input()
#         print('I am happy to hear that you are feeling ' + feeling + '.')

# # solution 2
# for timeOfDay in ['morning', 'afternoon', 'evening']:
#     print('Good ' + timeOfDay + '!')
#     print('How are you feeling?')
#     feeling = input()
#     print('I am happy to hear that you are feeling ' + feeling + '.')


# # solution 3
# def askFeeling(timeOfDay):
#     print('Good ' + timeOfDay + '!')
#     print('How are you feeling?')
#     feeling = input()
#     print('I am happy to hear that you are feeling ' + feeling + '.')
#     for timeOfDay in ['morning', 'afternoon', 'evening']:
#         askFeeling(timeOfDay)

# name = ""
# while name != "user":
#     print("Name:")
#     name = input()
# print("thanks")

# name = ""
# while True:
#     print("Name:")
#     name = input()
#     if name == "your name":
#         break
# print("thanks")

from statistics import mean

# try and catch
# numbers = []
# while True:
#     number = input("Enter a number: ")
#     # numbers.append(number)
#     if number == "done":
#         mean_numbers = mean(numbers)
#         print("The mean is {mean_numbers}")
#         break
#     try:
#         number == "done" and number == float(number)
#     except ValueError:
#         print("Invalid entry, please enter a number")

# mean_numbers = mean(numbers)
# print("The mean is {mean_numbers}")

numbers = []
while True:
    num_input = input("Enter a number or type 'done' to exit: ")
    if num_input == "done":
        break
    try:
        number = float(num_input)
    except ValueError:
        print("Invalid input, please enter a number or 'done'.")
    else:
        numbers.append(number)

mean_numbers = mean(numbers)
print(f"The mean is {mean_numbers}")
