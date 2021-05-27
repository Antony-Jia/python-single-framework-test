from fastapi import APIRouter, Depends, Path

    
router = APIRouter()

@router.get("/home")
async def home():
    return {"message": "Hello World123"}