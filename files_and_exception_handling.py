# print(1/0) #ZeroDivisionError: division by zero
#
# num = 9
# if num > 8:
#     print(num)

# # first iteration
# # Create a file with required permission and see what exceptions are possible
# file = open("order.text")  # opens takes a string arg with file name
# print(file) # FileNotFoundError

# second iteration
try:
    file = open("order.text")
    print("file found")  # try block required except or will throw an error
except FileNotFoundError as errmsg:  # creating alias
    print(f"FILE NOT FOUND: {errmsg}")
    # raise: throw back to user as is
finally:  # finally will always execute: used to clean up code
    print("Thanks for visiting")

# Create a file called order.text

# Apply DRY - OOP  - Python Packaging

