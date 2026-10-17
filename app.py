import streamlit as st

st.set_page_config(
    page_title="AI Verilog Debugger",
    page_icon="💻",
    layout="wide"
)

st.title("AI-Powered Verilog Debugger")
st.subheader("Analyze. Correct. Simulate. Verify.")

description = st.text_area(
    "Design Description",
    placeholder="Example: Design a 2-input AND gate"
)

faulty_code = st.text_area(
    "Faulty Verilog Code",
    height=180,
    placeholder="Paste your Verilog design here"
)

testbench = st.text_area(
    "Testbench Code",
    height=220,
    placeholder="Paste your Verilog testbench here"
)

if st.button("Debug Verilog", type="primary"):
    if description.strip() and faulty_code.strip() and testbench.strip():
        st.info("Inputs received. Next, we'll connect your AI debugger.")
    else:
        st.warning("Please fill in all three fields.")
