import streamlit as st
import subprocess
from pathlib import Path

st.title("Shader Demo")
st.write("This app demonstrates a simple GLSL shader using Pyglet and ModernGL.")

shader_image = Path(__file__).parent / "shader.png"
if shader_image.exists():
    st.image(str(shader_image), caption="Static Shader Preview")

if st.button("Launch Live Demo"):
    with st.spinner("Launching shader demo..."):
        subprocess.Popen(["python", "shadertest.py"]);
        st.success("Shader demo launched in a new window.")