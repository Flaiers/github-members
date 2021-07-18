#!/bin/bash
python_interpreter=""

read -p "Python interpreter: " python_interpreter
`$python_interpreter -m venv env`
source env/bin/activate

pip install -U pip
pip install -r requirements.txt

python manage.py migrate

cat start.py | ./manage.py shell