"""Utils

"""

from passlib.context import CryptContext
from pymongo import MongoClient

from constants import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.task_management


def get_user_by_email(email: str):
    """Get the user data by using mailid

    Args:
        email (str): Email id of the user.

    Returns:
        dict: Returns the user data
    """
    return db.users.find_one({"email": email})


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
