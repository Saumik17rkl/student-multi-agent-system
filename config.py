"""
Configuration for Student Multi-Agent System
--------------------------------------------
Stores constants and environment settings.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application metadata
APP_NAME = "Student Multi-Agent Architect & Builder"
VERSION = "1.0.0"

# LLM Configuration - Load from environment variables
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4-mini")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_MODEL_NAME = os.getenv("GROQ_MODEL_NAME", "llama-3.2-70b-instruct")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-2.0-flash-exp")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Application settings
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

# Validate required environment variables
required_vars = ["OPENAI_API_KEY", "GROQ_API_KEY", "GEMINI_API_KEY"]
missing_vars = [var for var in required_vars if not globals().get(var)]

if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
