
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class DietRequest(BaseModel):
    message: str

import openai

app = FastAPI()

# Set OpenAI API Key (Consider using environment variables for security)
openai.api_key = "YOUR_OPENAI_API_KEY"  # Placeholder for the API Key
def get_diet_suggestion(message):
    prompt = "suggest an indian diet with the following conditions " + message
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

@app.route('/suggest_diet', methods=['POST'])
def suggest_diet(data: DietRequest):
    
    message = data.message
    suggestion = get_diet_suggestion(message)
    return jsonify({"suggestion": suggestion})

if __name__ == '__main__':
    app.run(debug=True)

