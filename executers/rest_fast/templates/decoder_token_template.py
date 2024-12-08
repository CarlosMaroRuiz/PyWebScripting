DECODER_TOKEN_TEMPLATE = """from jose import JWTError, jwt
from fastapi import Request, HTTPException, status
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SecretKey")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

def get_current_user(request: Request) -> str:
    token = request.headers.get("Authorization")
    print(token)

    if not token or not token.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid or missing token"
        )

    token = token.split(" ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("correo")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Token missing 'correo'"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid token"
        )
"""
