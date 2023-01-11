from trame_client.widgets.core import AbstractElement
from . import module


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


class FileBrowser(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__(
            "filebrowser",
            **kwargs,
        )
        self._attr_names += [
            # ("histogram_data", "histogramData"),
            "attribute"
        ]
        self._event_names += [
            ("set_attribute", "setAttribute"),
        ]
