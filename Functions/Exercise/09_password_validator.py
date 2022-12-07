def password_validator(pw: str):
    validator = list()
    if not (6 <= len(pw) <= 10):
        validator.append("Password must be between 6 and 10 characters")

    if not pw.isalnum():
        validator.append("Password must consist only of letters and digits")

    digits_count = 0
    for i in pw:
        if i.isdigit():
            digits_count += 1
    if digits_count < 2:
        validator.append("Password must have at least 2 digits")

    return validator


password = input()
if len(password_validator(password)) == 0:
    print("Password is valid")
else:
    print("\n".join(password_validator(password)))


# def password_validate(password):
#     is_password_valid = True
#     # It should be 6 - 10 (inclusive) characters long
#     if not 6 <= len(password) <= 10:
#         is_password_valid = False
#         print("Password must be between 6 and 10 characters")
#     # It should consist only of letters and digits
#     is_legit = True
#     for char in password:
#         if not (char.isdigit() or char.isalpha()):
#             is_legit = False
#             is_password_valid = False
#             break
#     if not is_legit:
#         print("Password must consist only of letters and digits")
#     # It should have at least 2 digits
#     count_digits = 0
#     for char in password:
#         if char.isdigit():
#             count_digits += 1
#     if count_digits < 2:
#         print("Password must have at least 2 digits")
#         is_password_valid = False
#
#     if is_password_valid:
#         print("Password is valid")
#
#
# pass_word = input()
# password_validate(pass_word)
