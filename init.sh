#! bash
alias python='winpty python'
python manage.py makemigrations
python manage.py migrate
winpty python manage.py createsuperuser
