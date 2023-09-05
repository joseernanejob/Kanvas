


echo "Building the project..."
python -m pip install -r requirements.txt


echo "Make Migrations"
python manage.py makemigrations --noinput
python manage.py migrate --noinput


echo "Collect Static..."
python manage.py collectstatic --no-input --clear


echo "BUILD END"