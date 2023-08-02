#!/usr/bin/env python3
def validate_password(password):
    if len(password) < 8:
        return False

    has_uppercase=any([c.isupper()for c in password ])
    has_lowercase = any([c.islower() for c in password])
    has_digit     = any ([c.isdigit () for c in password])
    has_nospace = ' ' not in password
    
    return all((has_uppercase,has_lowercase,has_digit, has_nospace))
