import time
from pynput.mouse import Listener
import services.events_services as es
from datetime import datetime as dt
from models.event import Event
import cv2
import base64
from bson.binary import Binary

time_str_format = "%d-%m-%Y_%H:%M:%S:%f"
TIME = dt.now().strftime(time_str_format)
X = None
Y = None
img_name = ""
img_bytes: bytes = b""

def mouse(x, y, button, pressed):
    """Check if the left mouse button is clicked and take the picture from the webcam"""
    
    global X, Y
    button_str = button.name

    if pressed and button_str == "left":
        X, Y = x, y
        take_image(x, y)
        text = f"Time: {TIME} and mouse at ({x}, {y})"
        print(text, img_name)
    

def take_image(x, y):
    """The logic for capturing the image and recording to the database. 
        Uncomment line 56 if you want the pictures to be saved on the hard drive 
        (the default folder is where the repo code is cloned)"""

    global img_name, img_bytes, TIME
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    if not ret:
        print("failed to grab frame!")
        
    TIME = dt.now().strftime(time_str_format)
    _, buffer = cv2.imencode('.jpg', frame)
    img_bytes = base64.b64encode(buffer).decode('utf-8')
    
    # create the record in the database
    es.insert(
        Event(
            c_x=x,
            c_y=y,
            time=TIME,
            image_data=img_bytes))
    
    cap.release()
    img_name = f"frame_{TIME}.jpg"
    # cv2.imwrite(img_name, frame)  # uncommenting will enable writing the file on the hard drive
    print(f"{img_name} created!")
    

async def webcam_capture():
    """The purpose of this function is to return the X and Y values 
        so they can be displayed in the browser window"""
    
    with Listener(on_click=mouse) as listener:
        pass
    
    return X, Y
