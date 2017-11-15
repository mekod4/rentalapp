# rentalapp

This is a Movie Rental Aplication based on Angular JS and Django/Python. This application let you manage your movie rentales with one click and the Django Admin to manage your movie.

The REST is include.

You need to have Python installed on Machine. (Preferebly, 3.6 and above)

![alt text](screenshot/screenshot.png "")

#### Install the enviroment

Skip this step if you don't care about virtualenv
```
For Windows: pip install virtualenvwrapper-win
For Unix: pip install virtualenvwrapper
```

#### Install the project
```
$ git clone https://github.com/manuhazen/rentalapp.git
$ cd rentalapp
$ mkvirtualenv 'examplenamevirtualenv'
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

#### Dummy Data 

The project has some dummy data, if you want to use it run this step
```
$ python manage.py loaddata db.json
```

The application will be running in http://127.0.0.1:8000/