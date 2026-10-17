import os
import re
import subprocess
from pathlib import Path
import requests



def ask_gemini(prompt):
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "Please set the GEMINI_API_KEY environment variable."
        )

    url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-3.5-flash:generateContent"
    )

    response = requests.post(
        url,
        headers={"x-goog-api-key": api_key},
        json={"contents": [{"parts": [{"text": prompt}]}]},
        timeout=60,
    )
    response.raise_for_status()

    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def debug_verilog(description, faulty_design, testbench, testbench_module):
    prompt = f"""
You are a Verilog debugging assistant.

Design description:
{description}

Faulty Verilog design:
{faulty_design}

Testbench:
{testbench}

Explain the required circuit and provide a corrected Verilog design.
Return the complete design inside one ```verilog code block.
Do not include the testbench in the code block.
"""

    answer = ask_gemini(prompt)

    print("AI analysis and correction:\n")
    print(answer)

    match = re.search(
        r"```(?:verilog|systemverilog)?\s*\n(.*?)```",
        answer,
        re.DOTALL | re.IGNORECASE,
    )

    if not match:
        print("\nCould not extract Verilog code automatically.")
        return

    corrected = match.group(1).strip()

    Path("design.v").write_text(corrected)
    Path("testbench.v").write_text(testbench)

    compile_result = subprocess.run(
        [
            "iverilog", "-g2012", "-s", testbench_module,
            "-o", "simulation.out", "design.v", "testbench.v"
        ],
        capture_output=True,
        text=True,
        timeout=30,
    )

    if compile_result.returncode != 0:
        print("\nCompilation failed:")
        print(compile_result.stderr)
        return

    print("\nCompilation successful!")

    simulation = subprocess.run(
        ["vvp", "simulation.out"],
        capture_output=True,
        text=True,
        timeout=30,
    )

    print("\nSimulation output:")
    print(simulation.stdout)

    if simulation.returncode != 0:
        print("\nSimulation failed:")
        print(simulation.stderr)
    elif re.search(
        r"ALL\s+\d+\s+TESTS\s+PASSED",
        simulation.stdout,
        re.IGNORECASE,
    ):
        print("\nTestbench reports that all tests passed!")
    else:
        print("\nReview the testbench output to determine the result.")

