## Authentication system project 

This is a simple authentication system project built using python, Django, html and css! It
has function based view and some common functionalities like login, logout, registeration, email 
confirmation, password change and password reset.

you can set up this project as follow:
1- first run the following command in your terminal to clone the project
git clone https://github.com/sajadrajaee/authentication-system.git
2- get inside the folder where you can see manage.py file and create venv as follow:
  ```python -m venv .venv```
  ```.venv\Scripts\activate```
this will activate virtual envoirment for you
3- run the following command to install requirements of project: 
  ```pip install -r requirements.txt ```

4-now make migrations and migrate the changes to the database, run the following commands one by one:
  ```python manage.py makemigrations authe ```
  ```python manage.py migrate ```

5-the project setup is finished now and run that using the following command:
  ```python manage.py runserver```

note that this project is for educational purposes and feel free yourself to add other feature 
and edit as you want. 
