import random
import string

def generate_password(hint_words, length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    hint_string = "".join(hint_words)
    hint_chars = min(length, len(hint_string))
    password = ''.join(random.sample(hint_string, hint_chars))
    if len(password) < length:
        remaining_length = length - len(password)
        random_characters = ''.join(random.choices(characters, k=remaining_length))
        password += random_characters
    return password
hint_words = input("Enter hint words").split()
password_length = int(input("Enter the required password length: "))
password = generate_password(hint_words, password_length)
print("Generated Password is : ", password)
