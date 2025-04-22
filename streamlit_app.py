import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.title("Interactive Shader Demo")
st.write("This Streamlit app embeds a WebGL shader demo (Three.js & GLSL).")

html_file = Path(__file__).parent / "fractal.html"
if html_file.exists():
    components.html(html_file.read_text(), height=800, scrolling=True)
else:
    st.error("Could not find 'fractal.html'. Please ensure it exists.")