call venv\Scripts\activate.bat

set FLASK_APP=src/WebApi.py
git pull
python -m flask run
