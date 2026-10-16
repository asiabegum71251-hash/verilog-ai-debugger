import os
import requests

def ask_gemini(prompt):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Set GEMINI_API_KEY in your environment before running."
        )

    url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-3.5-flash:generateContent"
    )

    response = requests.post(
        url,
        headers={"x-goog-api-key": api_key},
        json={"contents": [{"parts": [{"text": prompt}]}]},
        timeout=60
    )
    response.raise_for_status()
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def debug_verilog(description, testbench):
    prompt = f"""
Analyze this Verilog project.

Design description:
{description}

Testbench:
{testbench}

Explain the required logic and suggest a corrected Verilog design.
Return the design in a verilog code block.
"""
    return ask_gemini(prompt)
