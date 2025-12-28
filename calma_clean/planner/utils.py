import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_ai_feedback(mood, energy, note):
    prompt = f"""
    User mood: {mood}
    User energy: {energy}
    Notes: {note}

    Give a short, friendly, and motivational feedback for the user.
    """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # أو GPT-4 لو متاح
            prompt=prompt,
            max_tokens=50,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "🤖 Sorry, AI feedback is unavailable right now."
