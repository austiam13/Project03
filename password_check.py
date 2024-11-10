"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = get_password()
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))



def get_password():
  return input(">")

def is_valid_password(password):
    if not check_length(password, MIN_LENGTH, MAX_LENGTH):
        return False
    if not contains_lower(password):
        return False
    if not contains_upper(password):
        return False
    if not contains_digit(password):
        return False
    if SPECIAL_CHARS_REQUIRED and not contains_special(password, SPECIAL_CHARACTERS):
        return False
    return True

def check_length(password,MIN_LENGTH,MAX_LENGTH):
  if MIN_LENGTH<len(password)<MAX_LENGTH:
      return True
  return False

def contains_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def contains_lower(password):
    for char in password:
        if char.islower():
            return True
    return False

def contains_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def contains_special(password, special_characters):
        for char in password:
            if char in special_characters:
                return True
        return False


main()
