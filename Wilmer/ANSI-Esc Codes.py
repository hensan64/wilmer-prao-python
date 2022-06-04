# ANSI-Esc Codes Are Used By Typing \ With Inserted Codes Below.
# The ANSI-Esc Modification Starts At The First Letter After The Code. To Stop The Modification, Insert The 'end' ANSI-ESC Code Mentioned Below.

end = "\033[0;0m"
white = "\033[0m"
red_bold = "\033[1;31m"
dark_red = "\033[91m"
green = "\033[92m"
blue = "\033[94m"
pink = "\033[95m"

ANSI_example = str(blue + "This is an example" + end + ".")
print(ANSI_example)