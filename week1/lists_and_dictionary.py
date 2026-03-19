# List of test users
test_users = ["standard_user" , 
              "locked_out_user" , 
              "problem_user" , 
              "performance_glitch_user" , 
              "error_user" , 
              "visual_user"]

# Print Each User
for user in test_users:
    print(f"Test Username: {user}")

# Dictionary of login credentials
credentials = {
    "username" : "standard_user",
    "password" : "secret_sauce",
    "role" : "customer",
            }

# Print each key/value pair
for key, value in credentials.items():
    print(f"{key} : {value}")