#!/usr/bin/python3
def raise_exception_msg(message=""):
    class NameException(Exception):
        pass

    raise NameException(message)

# Call the function to raise a name exception with a custom message
try:
    raise_exception_msg("This is a custom name exception.")
except NameException as e:
    print("Caught exception:", e)

