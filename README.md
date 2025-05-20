# Shader Demo

This project provides an interactive shader playground with both web-based and native demos:

- **Web Demo**: A Streamlit app wrapping WebGL shaders (Three.js & p5.js) allowing live parameter tweaking via JSON-driven controls.
- **Native Demo**: A standalone Pygame + ModernGL flame shader (`shad1.py`) with real-time uniforms (time, resolution, mouse).

---

## Table of Contents
- [Features](#features)
- [File Structure](#file-structure)
- [Controls Schema Format](#controls-schema-format)
- [Web Demo (Streamlit)](#web-demo-streamlit)
  - [Dynamic Uploads](#dynamic-uploads)
  - [Usage](#usage)
- [Native Demo (Pygame + ModernGL)](#native-demo-pygame--moderngl)
- [Deployment](#deployment)
- [Logs & Development Notes](#logs--development-notes)
- [Contributing & Future Work](#contributing--future-work)

---

## Features
- **JSON-driven UI**: Define shader parameters in a `controls.json` schema to auto-generate Streamlit widgets (sliders, etc.).
- **Dynamic Shader Templates**: Upload any HTML shader template at runtime to replace the default `fractal.html` or `fire2.html`.
- **Two Demo Backends**:
  - **Three.js** fractal shader in `fractal.html`.
  - **p5.js** fire shader in `fire2.html`.
- **Uniform Injection**: Sidebar values injected into GLSL `const float` and JS `let` defaults via regex.

---

## File Structure
```
.  
├─ Procfile               # Cloud run command: `streamlit run streamlit_app.py`
├─ README.md              # Project documentation
├─ requirements.txt       # Python dependencies
├─ controls.json          # Default schema for Three.js fractal demo
├─ fractal.html           # Three.js shader template
├─ fire2.json             # Schema for p5.js fire demo
├─ fire2.html             # p5.js shader template
├─ streamlit_app.py       # Main Streamlit application
├─ shad1.py               # Pygame + ModernGL standalone flame demo
├─ shader.png             # Static preview image (used by native demo docs)
├─ todo.md                # Roadmap and enhancements
├─ log.txt                # Release notes for interactive app features
└─ [*.log]                # Optional development session logs
```

---

## Controls Schema Format
Define each parameter in a JSON array with fields:
```json
{
  "name": "paramName",         // Identifier used in HTML/JS/GLSL
  "label": "Human Label",      // Sidebar widget label
  "widget": "slider",          // e.g., slider, selectbox, color_picker
  "type": "float",             // Data type: float, int, str
  "default": 1.0,                // Default value
  // For numeric widgets:
  "min": 0.0,
  "max": 2.0,
  "step": 0.01,
  // For select widgets:
  "options": [ "opt1", "opt2" ]
}
```
The app currently supports `slider` widgets for floats and ints; other widget types fall back to their default until implemented.

---

## Web Demo (Streamlit)

### Dynamic Uploads
Users can override both the controls schema and HTML template at runtime:
```python
json_uploader = st.sidebar.file_uploader("Upload controls.json", type=["json"])
html_uploader = st.sidebar.file_uploader("Upload fractal.html", type=["html"])
```
The app falls back to the local `controls.json` and `fractal.html` if no upload is provided.

### Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Tweak parameters in the sidebar; the shader updates in real time.

**Default Controls (fractal.html)**:
- `uvFractalScale`: float slider [0.5, 2.0], default 1.25  
- `uvOffset`: float slider [0.0, 1.0], default 0.50  
- `iterations`: int slider [1, 10], default 4  

**Fire Demo Controls (fire2.html)**:
- `fireHeight`: float slider [0.1, 5.0], default 1.0  
- `centerPower`: float slider [0.1, 5.0], default 1.0  
- `noiseScale`: float slider [0.001, 1.0], default 0.01  

---

## Native Demo (Pygame + ModernGL)
Launch `shad1.py` for an OpenGL flame shader demo in a resizable window:
- Uniforms: `iTime`, `iResolution`, `iMouse`  
- Dependencies: `pygame-ce`, `moderngl`, `numpy`  
```bash
pip install pygame-ce moderngl numpy
python shad1.py
```

---

## Deployment
For Heroku or Streamlit Cloud:
1. Ensure `Procfile` contains:
   ```
   web: streamlit run streamlit_app.py --server.port $PORT --server.headless true
   ```
2. Push to your Git remote; the platform will detect and run the web process.

---

## Logs & Development Notes
- **log.txt**: Release notes for the interactive app (upload logic, regex fixes, p5.js demo).  
- **Additional `.log` files**: Session journals for other shader experiments. Consider moving them to a `logs/` folder or adding to `.gitignore`.
- **todo.md**: Roadmap for JSON-driven widgets, remote synchronization, and other enhancements.

---

## Contributing & Future Work
- Extend widget factory to support `selectbox`, `color_picker`, `text_input`.  
- Improve uniform injection to handle more GLSL/JS patterns.  
- Add real-time remote sync (WebSocket/MQTT) for multi-device shader control.  
- Allow on-the-fly procedural noise generation via uploaded shader libraries.

## Converting an Existing Shader to Dynamic Upload Format

When you have a raw GLSL (Three.js) or p5.js shader that you’d like to plug into this app, use the following prompt template with Codex-CLI to generate a self-contained HTML and matching `controls.json` schema:

```text
Hi Codex-CLI!
I have a shader (attach your .frag/.vert, or include the code below).
Please:

1. Extract all `uniform` and `const float` (or `#define`) parameters.
2. For each parameter, propose:
   - A human-friendly name & label
   - A Streamlit widget type (e.g., slider, color_picker, number_input, selectbox)
   - Reasonable default, min, max, and step (for numeric), or options list (for selects).
3. Ask me to confirm which parameters to expose externally; leave the rest as internal (but document them in a sidebar legend).
4. Generate:
   a) `controls.json` with only the externally exposed parameters.
   b) A self-contained `shader.html` (or `p5.html`) that:
      - Inlines your vertex and fragment GLSL (or `<script type="x-shader">` tags)
      - Loads the schema & HTML via Streamlit’s file_uploader fallback
      - Injects external values into shader constants or JS `let` defaults
      - Renders the shader in a canvas using Three.js (or p5.js)
      - Displays a sidebar legend of “Internal Controls” (e.g., Time, Resolution, Mouse X/Y)
      - Integrates with the existing `streamlit_app.py` logic for uploads & injection

Please walk me through the mapping of uniforms → widgets, let me confirm, then output the final `controls.json` and `shader.html` files.
```