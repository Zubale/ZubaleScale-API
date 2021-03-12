# ZubaleScale-API

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)
+ [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>
 Python api for IOT communication with Avery-Weigh Tronix Scales

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

Install the the 3.6 version of [python](https://www.python.org/downloads/).

### Installing

To get running it is only needed to download the packages and run the files.

To install all the packages run. 

```
pip install -r requirements.txt
```

#### To run the flask app:

##### Windows

```
set FLASK_APP=WebApi.py
python -m flask run
```

##### Mac/Linux

```
export FLASK_APP=WebApi.py
python -m flask run
```

Then a flask app should start running on localhost:5000. Ready to be called with get 
## Usage <a name = "usage"></a>

This only runs locally if needed to run more data use a [recommended production](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment) or use [ngrok](ngrok.com/) for one device 
