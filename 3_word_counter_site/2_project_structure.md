# manage.py

helps us do top level admin things

py manage.py help - to see all things manage.py can do

# db.sqlite3

stores data - auto generated database

# **pycache**

internal auto generated files

# \_\_init.py

advance django thing

# settings.py

## BASE_DIR

Basic directory. Set to auto move to the current path.
We can set it to absolute if needed

## SECRET_KEY

Should not be displayed to other people. When pushing online

## DEBUG

For dev enviroment. It will show information on the project to help you debug i.e if you go to a non existing page.

However live we should keep it secret

## ROOT_URLCONF

Tells you where your initial url conf file is

## TEMPLATES

changing django code into html templates

## WSGI_APPLICATION

When hosting application online - how ppl can connect to it

## DATABASES

generating sql litle on start of the project

## AUTH_PASSWORD_VALIDATORS

What is required when somebody creates a new user from the password

# urls.py

## urlpatterns

where the user request should go after user browser request and what html to send back
