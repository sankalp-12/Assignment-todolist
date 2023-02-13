# Assignment for Dubdub.ai
Simple To-Do List Application using Python [Flask] and HTML, with SQLite as database.


## Docker image
```console
$ docker pull 5ankalp/todo:1.0.2
```

## Clone this repository
```console
https://github.com/sankalp-12/Assignment-todolist.git
cd Assignment-todolist
```

### Setup project with virtual environment

```console
$ python3 -m venv venv
```

Activate it
```console
$ . venv/bin/activate
```

or on Windows
```console
venv\Scripts\activate
```

Install Requirements [Note: Python version used is 3.8.10]
```console
$ pip install -r requirements.txt
```

Set environment variables in terminal
```console
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

or on Windows
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

Run the app
```console
$ flask run
```
