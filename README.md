 # Shader Demo
 
 This project demonstrates a simple GLSL shader using Pyglet and ModernGL.
 
 # Files
 - `shadertest.py`: Runs a live Pyglet window displaying the dynamic shader.
 - `shader.png`: Static screenshot of the shader demo.
 - `streamlit_app.py`: Streamlit app to preview the shader image and launch the live demo.
 - `requirements.txt`: Project dependencies.
 
 # Setup
 1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
 
 2. Run the live shader demo:
    ```bash
    python shadertest.py
    ```
 
 3. Launch the Streamlit app:
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