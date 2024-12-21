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
