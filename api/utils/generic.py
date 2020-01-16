# Django Imports
from django.contrib.auth.hashers import (Argon2PasswordHasher)
from django.utils.crypto import get_random_string

# Third Party Imports
from argon2.exceptions import (VerificationError, HashingError)


class HashPassword:

    def __init__(self, password):
        if not isinstance(password, str):
            raise ValueError("password should be instance of 'str' class.")
        self.password = password

    def get_hash(self):
        try:
            ph_obj = Argon2PasswordHasher()
            return ph_obj.encode(password=self.password, salt=get_random_string())
        except HashingError:
            raise HashingError("Provide valid data type for password.")

    def verify_hash(self, _hash):
        try:
            ph_obj = Argon2PasswordHasher()
            return ph_obj.verify(password=self.password, encoded=_hash)
        except VerificationError:
            return False
