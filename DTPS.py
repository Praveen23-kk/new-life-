import os
import requests

def translate_text(text, target_language):
    """Translates text using the Gemini API.

    Args:
        text: The text to translate.
        target_language: The target language code (e.g., "es", "fr", "de").

    Returns:
        The translated text, or None if there was an error.
    """

    api_key = os.environ.get("GEMINI_API_KEY")="AIzaSyDjv__iZGwG4eMKZk5Nd_idSFBbAMwZTXY" # Get API key from environment variables
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")


    base_url = "https://api.gemini.com/v1/translations"

    headers = {
        "Authorization": f"Bearer {AIzaSyDjv__iZGwG4eMKZk5Nd_idSFBbAMwZTXY}",
        "Content-Type": "application/json"  # Important for Gemini
    }

    data = {
        "text": text,
        "target_lang": target_language # Gemini uses lowercase language codes
    }

    try:
        response = requests.post(base_url, headers=headers, json=data)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)

        translated_data = response.json()
        
        if 'translated_text' in translated_data:  # Check the structure of Gemini's response
            return translated_data['translated_text']
        else:
            print("Error: 'translated_text' key not found in the response")
            print("Response content:", translated_data)  # Print the response for debugging
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error during translation: {e}")
        return None




if __name__ == "__main__":
    text_to_translate = "This is an example."
    target_lang = "es"  # Spanish

    try:
        translated_text = translate_text(text_to_translate, target_lang)
        if translated_text:
             print(f"Translated text: {translated_text}")
    except ValueError as e:
        print(f"Error: {e}")