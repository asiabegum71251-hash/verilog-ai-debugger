# AI-Powered Verilog Debugger

## Project Overview
An AI-assisted tool that analyzes a Verilog design using its
design description and testbench, suggests corrected Verilog
code, compiles the proposed design, and runs simulation tests.

## Technologies Used
- Python
- Google Gemini API
- Icarus Verilog
- Google Colab
- GitHub

## Workflow
1. Provide the design description and testbench.
2. Ask Gemini to analyze and correct the Verilog design.
3. Extract the proposed Verilog code.
4. Compile the design using Icarus Verilog.
5. Run the testbench and inspect the simulation results.

## Important Note
AI-generated code must be checked. Passing a testbench does not
guarantee correctness for every possible input.

## Security
Set GEMINI_API_KEY as a private environment variable.
Never upload API keys to GitHub.
