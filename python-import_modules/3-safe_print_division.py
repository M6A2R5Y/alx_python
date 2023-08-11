#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    finally:
        print("Inside result: {}".format(result) if 'result' in locals() else "Inside result: None")

    return result

# Test cases
print(safe_print_division(10, 2))
print(safe_print_division(10, 0))
print(safe_print_division(10, 'a'))

