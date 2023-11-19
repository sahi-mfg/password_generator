import random
import string
import logging

import sqlite3
import bcrypt


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


def create_connection():
    return sqlite3.connect("passwords.db")


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()


def save_password(password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO passwords (password) VALUES (?)",
        sanitize(hashed_password),
    )
    connection.commit()
    connection.close()


def sanitize(input_string):
    # Implement sanitization logic here
    sanitized_string = input_string.replace("'", "''")
    return sanitized_string
