# Third Party Imports
from argon2 import PasswordHasher
from argon2.exceptions import (VerificationError, HashingError)


class HashPassword:

    def __init__(self, password):
        if not isinstance(password, str):
            raise ValueError("password should be instance of 'str' class.")
        self.password = password

    def get_hash(self):
        try:
            ph_obj = PasswordHasher()
            return ph_obj.hash(password=self.password)
        except HashingError:
            raise HashingError("Provide valid data type for password.")

    def verify_hash(self, _hash):
        try:
            ph_obj = PasswordHasher()
            return ph_obj.verify(hash=_hash, password=self.password)
        except VerificationError:
            return False
