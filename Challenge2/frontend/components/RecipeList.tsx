"use client";


import React, { useEffect, useState } from 'react';

function RecipeList() {
  const [recipes, setRecipes] = useState([]);

  const ENDPOINT = process.env.NEXT_PUBLIC_ENDPOINT


  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const response = await fetch(`${ENDPOINT}/recepies/suggest`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setRecipes(data);
      } catch (error) {
        console.error('Error fetching recipes:', error);
      }
    };

    fetchRecipes();
  }, []);

  return (
    <ul>
      {recipes.map((recipe:any) => (
        <li key={recipe.id}>{recipe.name}</li>
      ))}
    </ul>
  );
}

export default RecipeList;