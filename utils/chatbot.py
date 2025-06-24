

# import google.generativeai as genai
# from config.config import GEMINI_API_KEY

# try:
#     genai.configure(api_key="AIzaSyA0XkLtOhUgwooQ0eT8niaPqyYTmptTHjQ")
#     # List available models to verify
#     available_models = [m.name for m in genai.list_models()]
#     print(f"Available models: {available_models}")
    
#     # Use a supported model from the list (e.g., gemini-1.5-pro-001)
#     model = genai.GenerativeModel('gemini-1.5-pro-001')
# except Exception as e:
#     raise Exception(f"Failed to configure Gemini API: {str(e)}")

# def get_learning_response(prompt):
#     try:
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         raise Exception(f"Error generating response: {str(e)}")









#api 
import httpx

# API Configuration
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Request headers
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:8501",  # for analytics (optional)
    "X-Title": "GenEDxAI"                     # your app/project name (optional)
}

# Core function to send prompt and get response
def get_learning_response(prompt):
    try:
        response = httpx.post(
            API_URL,
            headers=HEADERS,
            json={
                "model": "mistralai/mistral-7b-instruct:free",  # Free model available on OpenRouter
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            },
            timeout=20.0  # seconds
        )

        # Raise an error if the request failed (e.g., 400/500 status)
        response.raise_for_status()

        # Extract and return the assistant's message
        return response.json()['choices'][0]['message']['content']

    except Exception as e:
        raise Exception(f"Error generating response: {str(e)}")
