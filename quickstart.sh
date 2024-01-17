source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
cd rafael_web/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
