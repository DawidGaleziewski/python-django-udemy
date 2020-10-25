virtual env is a popular tool in django community.
virtual env allows to create a space for each project so that it has anything specific for this project in it.


## install virtualenv
pip3 install virtualenv

Good place to put venv is next to the project not in the project dir itself

may need to install it like sudo python3 -m virtualenv venv

# enter venv
source venv/bin/activate

in windows 
venv\Scripts\activate

# quit venv
deactivate

We can now proceed to install packages we need and start project

django-admin start-project portfolio

we will need to install django as well in our venv!