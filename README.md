 # Shader Demo
 
 This project demonstrates an interactive WebGL shader demo (Three.js & GLSL) embedded in a Streamlit app.
 
# Files
- `shad1.py`: Pygame + ModernGL (OpenGL) standalone flame shader demo.
- `fractal.html`: HTML + Three.js shader demo used by the Streamlit app.
- `streamlit_app.py`: Streamlit app embedding `fractal.html`.
- `requirements.txt`: Project dependencies.
 
# Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Launch the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
  
# Deployment
For cloud deployment (e.g. Streamlit Cloud or Heroku), ensure you launch the Streamlit app instead of the Pyglet demo:
1. Add a `Procfile` at the project root with:
   ```text
   web: streamlit run streamlit_app.py --server.port $PORT --server.headless true
   ```
2. Push your repo to your cloud platform; it will run the Streamlit app as the web process.