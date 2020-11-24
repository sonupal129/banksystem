
# BANK SYSTEM
[![N|Solid](https://economictimes.indiatimes.com/thumb/msid-71160696,width-1200,height-900,resizemode-4,imgsize-169788/bank-getty.jpg?from=mdr)](https://google.com/)

Basic Banking System
Features of service are below

  - Deposit money
  - Withdraw money
  - Balance enquiry
  - Export transaction reports
  - Send email/sms notification on every transaction

### Tech Used

Bank App runs on python version 3+:

* [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html) - Celery is a task queue implementation for Python web applications used to asynchronously execute work outside the HTTP request-response cycle.
* [Django](https://docs.djangoproject.com/en/3.1/) - Django is a Python-based free and open-source web framework that follows the model-template-views architectural pattern. It is maintained by the Django Software Foundation, an American independent organization established as a 501 non-profit.


### Installation

Bank App requires [python]([https://www.python.org/](https://www.python.org/)) v3+ to run.

Install the dependencies and devDependencies and start the server.

Go in directory where you want to setup project, Create virtual environment
```sh
$ virtualenv env -p python3
```
Activate virtual env
```sh
$ source env/bin/activate
```
Clone Project
```sh
$ git clone [project_url]
```
Go to project directory
```sh
$ cd project_directory
$ pip install -r requirements.txt
```
Create Database and update db details in settings.py
Now everything is setup & ready to run

Run celery workers
```sh
$ celery -A [project_name] worker -l info
```

Yay! app started successfully :smiley:
#### Happy Coding  :blush: