from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from utils.llm_helper import get_llm_response
from pydantic import BaseModel

router = APIRouter(
)

class ChatMessage(BaseModel):
    message: str

@router.post("/chatbot")
async def chat(chat_message: ChatMessage, db: Session = Depends(get_db)):
    ingredients = db.query(models.Ingredient).all()
    ingredient_list = [f"{i.name} ({i.quantity} {i.unit})" for i in ingredients]
    
    with open("data/my_fav_recipes.txt", "r") as f:
        recipes = f.read()
    
    response = await get_llm_response(
        chat_message.message,
        ingredient_list,
        recipes
    )
    
    return {"response": response} 