def test_import():
    from filebrowser.widgets.filebrowser import FileBrowser  # noqa: F401

    # For components only, the FileBrowser is also importable via trame
    from trame.widgets.filebrowser import FileBrowser  # noqa: F401,F811
