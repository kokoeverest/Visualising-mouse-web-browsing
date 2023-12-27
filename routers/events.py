from fastapi import APIRouter, Request, WebSocket
from fastapi.templating import Jinja2Templates
import services.events_services as es
from models.connection_manager import ConnectionManager
from utils.utils import webcam_capture, mouse
from pynput.mouse import Listener


app_router = APIRouter()
router = APIRouter(prefix = "/events")
manager = ConnectionManager()
templates = Jinja2Templates(directory="templates")


@app_router.get("/rec")
async def record_clicks(request: Request):

    """The mouse coordinates will be shown in the browser on left mouse click
        and events will be recorded in the database"""
    
    return templates.TemplateResponse("index.html", {"request": request})


@app_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    """The websocket which listens for the left mouse clicks and records the images to the database"""

    await manager.connect(websocket)
    try:
        with Listener(on_click=mouse) as listener:
            while True:
                x, y = await webcam_capture()  
                mouse_position = {"x": x, "y": y}
        
                # Send mouse position to the browser
                await websocket.send_json({"mouse_position": mouse_position})
    except:
        manager.disconnect(websocket)


@router.get("/")
def get_events(request: Request):

    """View all captured events in the browser"""

    all_events = es.get_all()
    for event in all_events:
        img_string = event.get("image_data").decode("utf-8")
        mime_type = "image/jpeg"
        event["image_data"] = f"data:{mime_type};base64,{img_string}"

    return templates.TemplateResponse("events.html", {"request": request, "all_events": all_events})


@router.delete("/clear") # accessible from Swagger:  http://127.0.0.1:8000/docs
def clear_db():

    """The database will soon get full of records and typing "y" at this endpoint will 
        wipe all the data"""
    
    answer = input("Type 'y' if you want to delete everything from the database?\n").lower()

    if answer == "y":
        action = es.clear_db()
        if action:
            print("Database cleaned!")
        return action
    
    return False