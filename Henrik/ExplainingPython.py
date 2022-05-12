# This is a comment.
#     It is used to explain things that are not obvious.
#     A comment is disregarded when executing a program, it is only text for documentation.

# This is a print statement, that prints to the CONSOLE
print("Printing something...")

# An empty print statement can be used to print an empty line
print()

# Code is colored to help telling you what type of information it is
#     Violet represents Python reserved keywords
#        'print' is a Python RESERVED word
#        NOTE: Variable names MUST NOT have the same name as a reserved keyword ('print' in this case)
#     Orange represents Python functions
#     Yellow represents Python function names
#     Orange represents Python functions


# A function is used when you want to do something many times,
#     without having to write the same code over and over again...
# A function is prefixed with 'def' and has to be DEFINED BEFORE (above) being called
def my_print_function(print_this):
    # 'print_this' above is called an ARGUMENT. An ARGUMENT is input information to a FUNCTION.
    print(print_this)  # Here we print what is sent into this function, that is the 'print_this' argument.


my_print_function("Print using my function once...")  # Here I am calling my own print function
my_print_function("Print using my function twice...")  # And again...
my_print_function("Print using my function third time...")  # And again...
