from fastapi import FastAPI
from .routers import recipes, ingredients, chatbot
from .db_init import init_db

app = FastAPI(title="Kitchen Buddy")

init_db()

app.include_router(recipes.router, prefix="/api/recipes", tags=["recipes"])
app.include_router(ingredients.router, prefix="/api/ingredients", tags=["ingredients"])
app.include_router(chatbot.router, prefix="/api/chatbot", tags=["chatbot"])

@app.get("/")
async def root():
    return {"message": "Welcome to Kitchen Buddy API"} 