# Day 31 Challenge:
# Create a program that checks if a given string is a valid email address.

from email_validator import validate_email, EmailNotValidError

# ask user to input email
user_email = input('Enter your email address: ')

try:
    # use validate_email function to check email, if valid print 'email valid'
    validate_email(user_email)
    print('Email valid')

    # if not valid, print 'invalid email' alongside reason for error
except EmailNotValidError as e:
    print(f'Invalid email: {e}')