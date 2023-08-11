#!/usr/bin/python3
def raise_exception():
    class CustomException(Exception):
        pass

    raise CustomException("Exception raised")
raise_exception()

