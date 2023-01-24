# Trame Widget: File Browser
This widget can be used in a trame project by the following procedure:

Clone this repository to your machine.
In your trame environment, perform an installation of this widget:
```
pip install [path/to/this/repository]
```

Invoke the trame Engine and UI classes for this widget in your trame project.
```
from filebrowser import engine as filebrowser_engine
...
filebrowser_engine.initialize(server, self.state, self.ctrl, self.vtk_pipeline)
```

```
from filebrowser.widget import FileBrowser
```

Run the trame application (follow instructions for that project).


## Development
After making changes to the vue component for the widget, be sure to build it for trame to use the compiled code. You may need to reinstall with pip in your trame environment if you did not install with the editable (`-e`) option.

### Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
