# BitFest 2025 Preliminary Challenge Solutions

This repository contains comprehensive solutions developed for the BitFest 2025 Preliminary Challenges, showcasing advanced natural language processing and intelligent recipe management systems.

## Challenge 1: Banglish-to-Bengali Transliteration Engine

An advanced sequence-to-sequence neural translation system that converts Romanized Bengali (Banglish) text into proper Bengali Unicode script. This solution enables seamless Bengali text generation without requiring specialized input methods.

### Key Features
- Leverages the SKNahin/bengali-transliteration-data dataset from Hugging Face
- Implements state-of-the-art mBART architecture for sequence-to-sequence translation
- Comprehensive evaluation with character-level accuracy metrics
- Optimized performance with mixed precision training
- Domain-adapted through fine-tuning on specialized Bengali transliteration corpus
- Robust handling of diverse Romanization patterns

### Technical Architecture
- Foundation Model: mBART-large
- Training Configuration:
  - Learning Rate: 3e-5
  - Batch Size: 8
  - Training Epochs: 5
  - Mixed Precision Training: Enabled
  - Gradient Accumulation Steps: 4

### Installation & Setup

## Challenge 2: Mofa’s Kitchen Buddy

Mofa loves cooking and frequently collects recipe pictures or posts from social media. He saves his favorite recipes in a dedicated folder. Mofa wants to build a backend system powered by a Large Language Model (LLM) that helps him manage his ingredients and suggests recipes based on what he has at home.

### Key Features
- **Database Schema for Ingredient Storage:** A database schema designed to efficiently store and manage available ingredients.
- **Ingredient Management API:** A set of APIs developed to facilitate the input and update of available ingredients, ensuring seamless management after shopping or cooking.
- **Recipe Retrieval and Storage:** A system capable of parsing and storing recipe details from both text and images into a single, comprehensive `my_fav_recipes.txt` file. Additionally, APIs are provided to input new favorite recipes in both text and image formats.
- **LLM-based Chatbot Integration:** Integration of a Large Language Model (LLM) powered chatbot that engages with users to understand their preferences and recommends recipes based on available ingredients at home.

### Technical Architecture
- **Database:** Utilizes a robust database management system to ensure efficient storage and retrieval of ingredients and recipe data.
- **API Framework:** Employs a fast and scalable API framework to handle ingredient management, recipe retrieval, and chatbot interactions.
- **Recipe Parsing:** Leverages advanced natural language processing (NLP) and optical character recognition (OCR) technologies to parse recipe details from both text and images.
- **Chatbot Technology:** Integrates a sophisticated LLM-based chatbot that processes user inputs and recommends recipes based on available ingredients and user preferences.
