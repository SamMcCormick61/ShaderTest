import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.title("Interactive Shader Demo")
st.write("This Streamlit app embeds a WebGL shader demo (Three.js & GLSL).")

html_file = Path(__file__).parent / "fractal.html"
if html_file.exists():
    # Sidebar controls to adjust shader parameters
    st.sidebar.header("Shader Controls")
    uv_fractal_scale = st.sidebar.slider(
        "UV Fractal Scale", min_value=0.5, max_value=2.0, value=1.25, step=0.01
    )
    uv_offset = st.sidebar.slider(
        "UV Offset", min_value=0.0, max_value=1.0, value=0.5, step=0.01
    )
    iterations = st.sidebar.slider(
        "Iterations", min_value=1, max_value=10, value=4, step=1
    )
    # Read and inject parameters into HTML
    html_content = html_file.read_text()
    html_content = html_content.replace(
        'const float uvFractalScale = 1.25;',
        f'const float uvFractalScale = {uv_fractal_scale};'
    )
    html_content = html_content.replace(
        'const float uvOffset = 0.5;',
        f'const float uvOffset = {uv_offset};'
    )
    html_content = html_content.replace(
        'const float iterations = 4.0;',
        f'const float iterations = {iterations}.0;'
    )
    components.html(html_content, height=800, scrolling=True)
else:
    st.error("Could not find 'fractal.html'. Please ensure it exists.")