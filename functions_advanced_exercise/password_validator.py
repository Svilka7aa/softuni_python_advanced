def password_validator(word):
    is_valid = True
    if len(word) < 6 or len(word) > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    if not word.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")

    if sum(map(lambda x: x.isdigit(), word)) < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


password = input()
password_validator(password)
