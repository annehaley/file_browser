from setuptools import setup

setup(
    name='filebrowser',
    version='1.0.0',
    packages=['filebrowser'],
    package_dir={'filebrowser': 'trame'},
    package_data={'filebrowser': ['build/*']},
    include_package_data=True,
)
