from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

users = []


@router.get("/")
async def read_user() -> list:
    return users


@router.post("/register/{username}", status_code=200)
async def read_users(username: str) -> str:
    users.append(username)
    return "ok"