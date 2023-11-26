import random
import string
import logging


def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        logging.warning("Please select at least one character type.")
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password
