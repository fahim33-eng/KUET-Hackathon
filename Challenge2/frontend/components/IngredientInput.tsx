"use client";

import React, { useState } from 'react';

function IngredientInput() {
  const [ingredient, setIngredient] = useState('');

  const ENDPOINT = process.env.NEXT_PUBLIC_ENDPOINT

  const handleAddIngredient = async () => {
    try {
      const response = await fetch(`${ENDPOINT}/ingredients`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: ingredient }),
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      setIngredient('');
      alert('Ingredient added successfully!');
    } catch (error) {
      console.error('Error adding ingredient:', error);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={ingredient}
        onChange={(e) => setIngredient(e.target.value)}
        placeholder="Enter ingredient"
      />
      <button onClick={handleAddIngredient}>Add</button>
    </div>
  );
}

export default IngredientInput;