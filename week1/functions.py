def check_pw_length(password, min_length=10):
    if len(password) >= min_length:
        return f"Password Minimum Length of {min_length}."
    else:
        return f"Password too short. Must be at least {min_length} characters long."

def check_username(username):
    if len(username.strip())>0:
        return f"Username Valid"
    else:
        return f"Please enter your Username."
    
def check_email_format(email):
    if "@" in email and "." in email:
        return f"{email} is valid."
    else: 
        return f"{email} is not a valid email format."
    
print(check_pw_length("secret_sauce"))
print(check_pw_length("123"))
print(check_username("standard_user"))
print(check_username(" "))
print(check_email_format("test@tester.com"))
print(check_email_format("badformat"))