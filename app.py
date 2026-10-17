import os
import io
import contextlib
import streamlit as st
import verilog_ai_debugger

st.set_page_config(
    page_title="AI Verilog Debugger",
    page_icon="💻",
    layout="wide"
)

# Load the API key securely from Streamlit Secrets
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

st.title("💻 AI-Powered Verilog Debugger")
st.subheader("Analyze. Correct. Simulate. Verify.")

st.write(
    "Enter your circuit description, faulty Verilog design, "
    "and testbench. The AI will suggest a correction and run a simulation."
)

description = st.text_area(
    "1. Design Description",
    placeholder="Example: Design a 2-input AND gate"
)

faulty_code = st.text_area(
    "2. Faulty Verilog Code",
    height=180,
    placeholder="Paste your Verilog design here"
)

testbench = st.text_area(
    "3. Testbench Code",
    height=220,
    placeholder="Paste your Verilog testbench here"
)

testbench_module = st.text_input(
    "4. Testbench module name",
    value="tb_and_gate",
    help="Enter the exact module name declared in your testbench."
)

if st.button("🚀 Debug Verilog", type="primary"):
    if not all([
        description.strip(),
        faulty_code.strip(),
        testbench.strip(),
        testbench_module.strip()
    ]):
        st.warning("Please fill in all four fields.")
    else:
        output = io.StringIO()

        try:
            with st.spinner("AI is analyzing your Verilog code..."):
                with contextlib.redirect_stdout(output):
                    verilog_ai_debugger.debug_verilog(
                        description,
                        faulty_code,
                        testbench,
                        testbench_module
                    )

            st.subheader("Debugging and Simulation Results")
            st.code(output.getvalue(), language="text")

        except Exception as error:
            st.error(f"Debugging failed: {error}")
            captured = output.getvalue()
            if captured:
                st.code(captured, language="text")
