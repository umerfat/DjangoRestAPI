# DjangoRestAPI

## Description
Sample Django REST API developed using Python and Django REST Framework. Uses Movie model as sample data

### Creating Project
django-admin startproject DjangoRestAPI

### Creating app inside project
django-admin startapp movieproject

### Running Server
python3 manage.py runserver

### Doing Migration (process of creating table out of Django models)
* ```python3 manage.py makemigrations``` #Checks if new models have been created
* ```python3 manage.py migrate``` # Creates actual tables out of models

### Create super user to access already available DjangoAdmin UI
* ```python3 manage.py createsuperuser```

## Pushing to Git
#### push an existing repository from the command line
* echo "#DjangoRestAPI" >> README.md
* ```git init```
* ```git add README.md```
* ```git commit -m "first commit"```
* ```git branch -M master```
* ```git remote add origin https://github.com/umerfat/DjangoRestAPI.git```
* ```git push -u origin master```


#### create a new repository on the command line
* ```git init```
* ```git add README.md```
* ```git commit -m "first commit"```
* ```git branch -M master```
* ```git remote add origin https://github.com/umerfat/DjangoRestAPI.git```
* ```git push -u origin master```

