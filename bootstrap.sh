#!/bin/sh
export FLASK_APP=app.py
venv/bin/flask --debug run -h 0.0.0.0
