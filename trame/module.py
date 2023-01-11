import os
from pathlib import Path

# Compute local path to serve
serve_path = str(Path(__file__).with_name("build").resolve())

# Serve directory for JS/CSS files
serve = {"__filebrowser": serve_path}
serve_files = os.listdir(serve_path)

scripts = [
    '__filebrowser/' + p for p in serve_files
    if str(p).endswith('.js') or str(p).endswith('.js.map')
]
styles = [
    '__filebrowser/' + p for p in serve_files
    if str(p).endswith('.css')
]

vuetify_config = {}
vue_use = ["filebrowser", ("trame_vuetify", vuetify_config)]

# Uncomment to add entries to the shared state
state = {}


# Optional if you want to execute custom initialization at module load
def setup(app, **kwargs):
    """Method called at initialization with possibly some custom keyword arguments"""
    pass
