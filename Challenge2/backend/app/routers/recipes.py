from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
from utils.recipe_parser import parse_recipe_text, parse_recipe_image
from pydantic import BaseModel

router = APIRouter(
)

class RecipeBase(BaseModel):
    name: str
    instructions: str
    cuisine_type: str
    preparation_time: int
    taste_tags: str
    reviews: float

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    
    class Config:
        orm_mode = True

@router.post("/recepies", response_model=Recipe)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    db_recipe = models.Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@router.post("/recepies/upload")
async def upload_recipe(file: UploadFile = File(...)):
    if file.content_type.startswith('image/'):
        recipe_text = await parse_recipe_image(file)
    else:
        recipe_text = await parse_recipe_text(file)
    
    with open("data/my_fav_recipes.txt", "a") as f:
        f.write(recipe_text + "\n\n")
    
    return {"message": "Recipe added successfully"}

@router.get("/recepies/suggest")
def suggest_recipes(db: Session = Depends(get_db)):
    available_ingredients = db.query(models.Ingredient).all()
    ingredient_names = [ing.name for ing in available_ingredients]
    
    recipes = db.query(models.Recipe).all()
    suitable_recipes = []
    
    for recipe in recipes:
        recipe_ingredients = recipe.instructions.lower()
        if all(ing.lower() in recipe_ingredients for ing in ingredient_names):
            suitable_recipes.append(recipe)
    
    return suitable_recipes 