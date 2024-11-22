import openai

openai.api_key = "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"

def generate_feedback(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """
    Generate feedback using GPT.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert sales analyst."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating feedback: {str(e)}"
