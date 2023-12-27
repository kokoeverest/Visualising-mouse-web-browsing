# Capturing mouse clicks and web cam frames in a web environment
```
A small Python API for capturing frames (images) and mouse coordinates (x, y) 
from the default webcam on a computer. Images are captured on left mouse click only 
and time of the click is also saved. 

All values are stored locally in a MongoDB database and can be accessed via browser 
when the server is running.

This API is created and tested on Ubuntu 22.04 so it might not work as expected on a 
different OS.

```
### * Technologies used - Fast API, Jinja2, WebSockets, OpenCV, Pynput, MongoDB 

## Packages installation and configuration of MongoDB

The work of the app relies on a connection to a MongoDB database. If you don't have it 
installed and configured on your machine you can follow these comprehensive instructions:

(https://www.cherryservers.com/blog/install-mongodb-ubuntu-22-04)

Connection to the database is established via environment variables:
```
"MONGODB_USERNAME"="your_db_username"
"MONGODB_PASSWORD"="your_db_password"
```
It is recommended to run this API in a virtual environment so it doesn't conflict with 
other 
packages on your system.

Sample commands to create a venv (virtual environment). *Requires the venv package, 
which is usually incuded in python default packages (if the first command throws an 
error, you probably don't have the venv package installed):

#### python3 -m venv test_env

#### source test_env/bin/activate

#### pip install --upgrade pip

Ensure that the virtual environment is active!

Then navigate to the root directory of the cloned project, where the requirements.txt 
should be found:

#### pip install -r requirements.txt

Start the server (you should be at the same folder, where the main.py file is!):

#### uvicorn main:app

If everything is ok you should see output on the console, similar to this:
```
INFO:     Started server process [355547]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Open a browser tab and go to http://127.0.0.1:8000/events/

#### You should see "No events recorded yet"

To record mouse events go to http://127.0.0.1:8000/rec

On every click with the left mouse button a frame should be captured and stored in 
the database.
To stop this process simply close the browser tab (one more frame will be captured 
on exit :) )

Go to http://127.0.0.1:8000/events/ again and you should see a list of all the 
images that were captured.

#### Cleaning the database:
An endpoint for cleaning the database is added 
(it was very useful during development :) )
It is accessible from http://127.0.0.1:8000/docs while the server is running.

On expanding of the endpoint menu - click "Try:, then "Execute". Then you should 
confirm that you really want to proceed - type "y" in the console - a confirmation 
message will appear if the operation was successful.

## Thank you for your interest!