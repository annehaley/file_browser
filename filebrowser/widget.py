from trame_client.widgets.core import AbstractElement
from . import module

__all__ = [
    'FileBrowser',
]


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


# -----------------------------------------------------------------------------
# FileBrowserWidget
# -----------------------------------------------------------------------------
class FileBrowser(HtmlElement):
    """
    The FileBrowser widget for trame can be used in "Save" mode (default) or "Open" mode.
    In Save mode, the widget requires a list of all applicable types for the file about to be saved.
        Each item in the file types list should be a dictionary containing the following keys:
        "value" (for the file extension string, beginning with ".")
        "text" (for the name of the file type, as should appear in the file type select box)
    The widget requires a list of possible directory paths for both local and remote locations.
    The user may select a current directory for both local and remote locations.
    When either current directory is changed, the values for the current directory contents should be re-evaluated.
    Directory contents should come as a list of files, folders, and groups.

    :param mode: String containing either "Save" or "Open"
    :type mode: str
    :param dark: true for dark UI mode, false otherwise
    :type dark: bool
    :param file_types: List containing file types applicable to the current file (in Save mode only).
    :param file_types: list[{value: string, text: string}]

    :param local_directories: List of all possible local directory paths
    :type local_directories: list[str]
    :param remote_directories: List of all possible remote directory paths
    :type remote_directories: list[str]

    :param current_local_dir: Current local directory path
    :type current_local_dir: str
    :param current_remote_dir: Current remote directory path
    :type current_remote_dir: str

    :param current_local_dir_contents: Contents of current local directory
    :type current_local_dir_contents: list[str]
    :param current_remote_dir_contents: Contents of current reomte directory
    :type current_remote_dir_contents: list[str]

    :param set_local_dir: Event triggered when user changes the current local dir
    :type set_local_dir: Function or JS expression (event)
    :param set_remote_dir: Event triggered when user changes the current remote dir
    :type set_remote_dir: Function or JS expression (event)

    Events:

    :param submit: Event triggered when user clicks the submit button, either to Save or to Open
    :type submit: Function or JS expression (event)
    """

    def __init__(self, **kwargs):
        super().__init__(
            "file-dialog",
            **kwargs,
        )
        self._attr_names += [
            "mode",
            "dark",
            ("file_types", "fileTypes"),
            ("local_directories", "localDirectories"),
            ("remote_directories", "remoteDirectories"),
            ("current_local_dir", "currentLocalDir"),
            ("current_remote_dir", "currentRemoteDir"),
            ("current_local_dir_contents", "currentLocalDirContents"),
            ("current_remote_dir_contents", "currentRemoteDirContents"),
        ]
        self.event_names = [
            ("set_local_dir", "setLocalDir"),
            ("set_remote_dir", "setRemoteDir"),
            "submit",
        ]
