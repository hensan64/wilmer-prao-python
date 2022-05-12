# This is a comment.
# It is used to explain things that are not obvious.
# A comment is disregarded when executing a program, it is only text for documentation.

print("This is a print statement on SCRIPT LEVEL (no indentation on the left)")
print()  # An empty print statement can be used to print an empty line

print("Code is colored to tell what type of information it is")
print("Violet represents Python reserved keywords")
print("    'print' is a Python RESERVED word")
print("    For example, variable names MUST NOT have the same name as a reserved keyword ('print' in this case)")
print("Orange represents Python functions")
print("Yellow represents Python function names")
print("Orange represents Python functions. Variable names MUST NOT have the same name ('print' in thist case)")

print()
print("A function is used when you want to do something many times,")
print("    without having to write the same code over and over again...")


def my_print_function(print_this):
    # 'print_this' above is called an ARGUMENT.
    # An ARGUMENT is input information to a FUNCTION.
    print(print_this)  # Here we print what is sent into this function, that is the 'print_this' argument.


print()
my_print_function("Here I am calling my_print_function")  # Here I am calling my own print function
my_print_function("A function is prefixed with 'def' and has to be DEFINED BEFORE being called")
my_print_function("    The call has to be below function)!")
