"""Auth

Raises:
    HTTPException: _description_
    credentials_exception: _description_
    credentials_exception: _description_
    credentials_exception: _description_

Returns:
    _type_: _description_
"""

from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from .models import User
from .utils import get_user_by_email, verify_password

router = APIRouter()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """create_access_token

    Args:
        data (dict): _description_
        expires_delta (Optional[timedelta], optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/token", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """login_for_access_token

    Args:
        form_data (OAuth2PasswordRequestForm, optional): _description_. Defaults to Depends().

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    user = get_user_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/verify-token")
def verify_token(token: str):
    """
    API to verify if the JWT token is valid.
    :param token: The JWT token as a string.
    """
    try:
        # Decode and verify the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": "Token is valid", "payload": payload}
    except JWTError as e:
        # Handle invalid or expired token
        raise HTTPException(status_code=401, detail="Invalid or expired token") from e

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """get_current_user

    Args:
        token (str, optional): _description_. Defaults to Depends(oauth2_scheme).

    Raises:
        credentials_exception: _description_
        credentials_exception: _description_
        credentials_exception: _description_

    Returns:
        _type_: _description_
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError as exc:
        raise credentials_exception from exc
    user = get_user_by_email(email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """get_current_active_user

    Args:
        current_user (User, optional): _description_. Defaults to Depends(get_current_user).

    Returns:
        _type_: _description_
    """
    # if current_user.disabled:
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
