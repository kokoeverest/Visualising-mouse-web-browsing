from data.db_init import database as db
from models.event import Event


def get_all():
    lst = db.find()
    events = [x for x in lst]

    return events


def insert(ev: Event):
    db.insert_one({"x": ev.c_x, 
                   "y": ev.c_y,  
                   "time": ev.time,
                   "image_data": ev.image_data})


def clear_db():
    events = get_all()
    try:
        for ev in events:
            ev_id = ev["_id"]
            db.delete_one({'_id': ev_id})
        return True
    except:
        return False
    