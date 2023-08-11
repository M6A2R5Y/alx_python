#!/usr/bin/python3
def raise_exception_msg(message=""):
    class NameError(Exception):
        pass

    raise NameError(message)

# Call the function to raise a name exception with a custom message
try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

