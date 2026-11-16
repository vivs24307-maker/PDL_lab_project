"""
Entry point for hosting Chronos on a real web server (for example PythonAnywhere).

Web servers do not run "python app.py". Instead they import a variable called
"application" from a file like this one and send every web request to it.
For running on your own computer, keep using:  python app.py
"""
import os
import sys

# Make sure Python can find app.py and the core/ folder next to this file
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from app import app as application  # noqa: E402
