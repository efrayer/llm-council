"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY is not set. Add it to backend/.env")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "openai/gpt-6.1-terra",
    "google/gemini-4-argon",
    "anthropic/claude-sonnet-5.5"
]

# Previous council - uncomment to switch back
# COUNCIL_MODELS = [
#     "openai/gpt-5.1",
#     "google/gemini-3.1-flash-lite-preview",
#     "anthropic/claude-sonnet-4.5"
# ]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "openai/gpt-6.1-sol"

# Previous chairmen - uncomment one to switch back
# CHAIRMAN_MODEL = "openai/gpt-6-astra"
# CHAIRMAN_MODEL = "anthropic/claude-sonnet-4.5"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
