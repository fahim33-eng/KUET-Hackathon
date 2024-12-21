import openai 

openai.api_key = "your-openai-api-key"

async def get_llm_response(user_message, ingredient_list, recipes):
    prompt = (
        f"You are a helpful kitchen assistant. The user has the following ingredients available: "
        f"{', '.join(ingredient_list)}. Here are some recipes they have saved:\n{recipes}\n\n"
        f"User: {user_message}\n"
        f"Assistant:"
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=prompt,
            max_tokens=150,  
            n=1,
            stop=None,
            temperature=0.7  
        )

        llm_response = response.choices[0].text.strip()
        return llm_response

    except Exception as e:
        print(f"Error calling LLM API: {e}")
        return "I'm sorry, I couldn't process your request at the moment."
