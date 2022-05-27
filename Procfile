web: gunicorn best_solver.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate