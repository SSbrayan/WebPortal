--Install Django
	??
	
--Check Django Version
	python -m django --version
	
--Create a Project
	python -m django startproject ValidationSite
	
--Run Server
	python manage.py runserver
	
--Change Port
	python manage.py runserver 8080
	
--Create the Polls app
	python manage.py startapp polls
	

	
--------MIGRATIONS----------

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.