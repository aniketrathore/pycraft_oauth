# Third Party Imports
from argon2 import PasswordHasher
from argon2.exceptions import (VerificationError, HashingError)


class HashPassword:

    def __init__(self, password):
        self.password = password

    def get_hash(self):
        try:
            ph_obj = PasswordHasher()
            return ph_obj.hash(password=self.password)
        except HashingError:
            raise HashingError("Provide valid password. It should not be None or empty value.")

    def verify_hash(self, _hash):
        try:
            ph_obj = PasswordHasher()
            return ph_obj.verify(hash=_hash, password=self.password)
        except VerificationError:
            raise VerificationError("Password did't match.")
