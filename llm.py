from nt import O_RDONLY
import requests
import json
from config import LM_STUDIO_URL, MODEL_NAME, GOAL

def ask_model(image_b64, history):
    prompt = f"""
You are controlling a computer.

Goal: 
{GOAL}

Return ONLY valid JSON:
{{
    "action": "click | double_click | type | press | scroll | done",
    "x": number,
    "y": number,
    "text": "",
    "done": false
}}

Rules:
- one action only
- use screen coordinates
- be precise
