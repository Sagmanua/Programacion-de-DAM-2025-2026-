import os
from openai import OpenAI

# It's good practice to verify the key exists before calling the client
api_key = os.environ.get("OPENAI_KEY")

if not api_key:
    print("Error: OPENAI_KEY not found in environment variables.")
else:
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Corrected model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Explain the three-body problem in simple terms."}
            ],
            temperature=0.3
        )
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"An error occurred: {e}")