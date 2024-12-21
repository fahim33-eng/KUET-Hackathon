from fastapi import UploadFile
import pytesseract
from PIL import Image
import io
import re

async def parse_recipe_text(file: UploadFile) -> str:
    """
    Parse recipe from a text file.
    Handles common text file formats and extracts structured recipe information.
    """
    content = await file.read()
    text = content.decode('utf-8')
    
    # Basic cleaning and formatting
    cleaned_text = clean_recipe_text(text)
    
    return cleaned_text

async def parse_recipe_image(file: UploadFile) -> str:
    """
    Parse recipe from an image file using OCR.
    Converts image to text and structures the recipe information.
    """
    # Read image file
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    
    # Perform OCR
    text = pytesseract.image_to_string(image)
    
    # Clean and format the extracted text
    cleaned_text = clean_recipe_text(text)
    
    return cleaned_text

def clean_recipe_text(text: str) -> str:
    """
    Clean and structure raw recipe text.
    Attempts to identify and format:
    - Recipe name
    - Ingredients list
    - Instructions
    - Metadata (prep time, cuisine type, etc.)
    """
    # Remove extra whitespace and normalize line endings
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Try to identify recipe sections
    sections = {
        'name': extract_recipe_name(text),
        'ingredients': extract_ingredients(text),
        'instructions': extract_instructions(text),
        'metadata': extract_metadata(text)
    }
    
    # Format the recipe in a consistent structure
    formatted_recipe = format_recipe(sections)
    
    return formatted_recipe

def extract_recipe_name(text: str) -> str:
    """Extract recipe name from text."""
    # Look for title-like text at the start
    lines = text.split('\n')
    for line in lines[:3]:  # Check first 3 lines
        if len(line.strip()) > 0 and len(line.strip()) < 100:  # Reasonable title length
            return line.strip()
    return "Untitled Recipe"

def extract_ingredients(text: str) -> list:
    """Extract ingredients list from text."""
    ingredients = []
    # Look for common ingredient patterns
    ingredient_pattern = r'(?i)(?:\d+(?:/\d+)?(?:\s*-\s*)?\s*(?:cup|tablespoon|teaspoon|tbsp|tsp|oz|pound|lb|g|ml|piece|pieces|to taste)[s]?\s+)?([a-zA-Z\s]+)'
    matches = re.finditer(ingredient_pattern, text)
    for match in matches:
        if match.group(1):
            ingredients.append(match.group(0).strip())
    return ingredients

def extract_instructions(text: str) -> list:
    """Extract cooking instructions from text."""
    instructions = []
    # Look for numbered steps or paragraph breaks
    step_pattern = r'(?:\d+\.|Step\s+\d+:?|\n\n)(.+?)(?=(?:\d+\.|Step\s+\d+:?|\n\n|$))'
    matches = re.finditer(step_pattern, text, re.DOTALL)
    for match in matches:
        if match.group(1):
            instructions.append(match.group(1).strip())
    return instructions

def extract_metadata(text: str) -> dict:
    """Extract recipe metadata like prep time, cuisine type, etc."""
    metadata = {}
    
    # Look for common metadata patterns
    time_pattern = r'(?i)(?:prep|cooking|total)\s+time:\s*(\d+)\s*(?:min|minutes|hrs|hours)'
    cuisine_pattern = r'(?i)cuisine:\s*([a-zA-Z\s]+)'
    
    # Extract prep time
    time_match = re.search(time_pattern, text)
    if time_match:
        metadata['prep_time'] = time_match.group(1)
    
    # Extract cuisine type
    cuisine_match = re.search(cuisine_pattern, text)
    if cuisine_match:
        metadata['cuisine_type'] = cuisine_match.group(1).strip()
    
    return metadata

def format_recipe(sections: dict) -> str:
    """Format recipe sections into a consistent string format."""
    formatted = f"Recipe: {sections['name']}\n\n"
    
    if sections['metadata']:
        formatted += "Metadata:\n"
        for key, value in sections['metadata'].items():
            formatted += f"{key}: {value}\n"
        formatted += "\n"
    
    if sections['ingredients']:
        formatted += "Ingredients:\n"
        for ingredient in sections['ingredients']:
            formatted += f"- {ingredient}\n"
        formatted += "\n"
    
    if sections['instructions']:
        formatted += "Instructions:\n"
        for i, instruction in enumerate(sections['instructions'], 1):
            formatted += f"{i}. {instruction}\n"
    
    return formatted 