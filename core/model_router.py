"""
Model Router
------------
Handles multi-model inference with fallback order:
1. OpenAI GPT
2. Gemini
3. Groq
"""

import logging
from utils.error_handlers import APIError

logger = logging.getLogger(__name__)

def query_model(prompt, context=None):
    context = context or {}
    try:
        # Try OpenAI / GPT-based response first
        from openai import OpenAI
        client = OpenAI()
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return resp.choices[0].message.content

    except Exception as e1:
        logger.warning(f"Primary model failed: {e1}. Falling back to Gemini...")

        # Try Gemini fallback
        try:
            import google.generativeai as genai
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-2.0-flash-exp")
            resp = model.generate_content(prompt)
            return resp.text

        except Exception as e2:
            logger.warning(f"Gemini failed: {e2}. Falling back to Groq...")

            # Try Groq fallback
            try:
                from groq import Groq
                client = Groq(api_key=os.getenv("GROQ_API_KEY"))
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.2-70b-instruct",
                )
                return chat_completion.choices[0].message.content

            except Exception as e3:
                logger.error(f"All models failed: {e3}")
                raise APIError("All AI backends are unavailable. Please try again later.", 503)
