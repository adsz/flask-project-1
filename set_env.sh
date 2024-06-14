#!/bin/bash
PYTHON_ENV="venv"
echo $PYTHON_ENV
python3 -m venv $PYTHON_ENV
source $PYTHON_ENV/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt

echo " "
pip list
