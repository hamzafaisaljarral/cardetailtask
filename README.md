# cardetailtask
# cardetailtask
-python3 -m venv djangoenv 
-source djangoenv/bin/activate
-pip3 install -t requirements.txt
-python manage.py migrate
-python manage.py runserver 8000

- there are four restfull api which return json response 
- all/  List all makes, models, and submodels
- car/ List all cars with their matching make, model and submodel names
- addcar/ Add new cars and enforce consistency of the inserted data directly in the database
- searchcar/ it take two parameter {price , mileage}
  return a list of matches sorted by `updated_at` 
