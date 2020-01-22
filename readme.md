Running the app

Preferably, first create a virtualenv and activate it, perhaps with the following command:

virtualenv -p python3 venv
source venv/bin/activate
Next, run

pip install -r requirements.txt
to get the dependencies.

Next, initialize the database

python manage.py seed_db