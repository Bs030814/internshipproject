from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
import sqlite3

app = FastAPI()

DATABASE_NAME = "login.db"

with sqlite3.connect(DATABASE_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS login (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """
    )


class LoginRequest(BaseModel):
    username: str
    password: str
    hashed_password: str = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(username: str, expires_delta: timedelta = timedelta(minutes=30)) -> str:
    expire = datetime.utcnow() + expires_delta
    encoded_jwt = jwt.encode({"sub": username, "exp": expire}, "secret_key", algorithm="HS256")
    return encoded_jwt


@app.post("/login")
def login(request: LoginRequest):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM login WHERE username = ?", (request.username,))
        result = cursor.fetchone()

        if result is None:
            raise HTTPException(status_code=400, detail="Invalid username or password")

        stored_password = result[2]

    if not verify_password(request.password, stored_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token = create_access_token(request.username)
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

    return {"message": "Access granted"}
