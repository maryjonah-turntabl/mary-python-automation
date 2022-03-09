from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='click_tools',
    version='0.0.0',
    py_modules=['file_concat'],
    install_requires=[
        'Click',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'concat_files=file_concat:concat_files',
            'confirm_ttlbr=confirm_ttblr:login'
        ]
    }
)