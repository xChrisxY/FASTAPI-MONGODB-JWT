from fastapi import APIRouter, HTTPException, status
from app.models.User import User
from app.services.user import find_user, create_user, verify_password_user, create_token_user

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/register", status_code=status.HTTP_201_CREATED, response_model=dict)
async def register_user(user: User):
    existing_user = await find_user(user.username)
    if existing_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    if existing_user is True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    result = await create_user(user)
    if result is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Can't add user")
    
    return {
        "message" : "User registered succesully",
        "user": result
    }

@auth_router.post("/login", status_code=status.HTTP_200_OK, response_model=dict)
async def login_user(username: str, password: str):
    existing_user = await find_user(username)
    if existing_user is None or existing_user is False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    verify_password = await verify_password_user(existing_user, password)
    if not verify_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = await create_token_user(existing_user)

    

    
