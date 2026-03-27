import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
PLANNER_MODEL = os.getenv("PLANNER_MODEL", "gpt-5-mini")
DESIGNER_MODEL = os.getenv("DESIGNER_MODEL", "gpt-5-mini")
BUILDER_MODEL = os.getenv("BUILDER_MODEL", "gpt-5-mini")
OPERATOR_MODEL = os.getenv("OPERATOR_MODEL", "gpt-5-mini")
