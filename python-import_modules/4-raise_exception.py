#!/usr/bin/python3
def raise_exception():
    class CustomException(Exception):
        pass

    raise CustomException("This is a custom type exception.")

# Call the function to raise the custom exception
raise_exception()

