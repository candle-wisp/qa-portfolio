# Test password format
import logging

logging.basicConfig(filename="test_errors.log", level=logging.ERROR)

credentials = {
    "username" : "standard_user",
    "password" : "secret_sauce"
}

try:
    role = credentials["role"]
except KeyError as e:
    print(f"Key Error: {e} role not available on this account.")
    logging.error(f"Key Error: {e} role not available on this account.")