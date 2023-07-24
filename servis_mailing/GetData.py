from sqlalchemy import  create_engine,desc,asc
from sqlalchemy.orm import Session,sessionmaker
from model import Message,User
from datetime import datetime


engine = create_engine('sqlite:///MassEmail.db', connect_args={'check_same_thread': False})
ses = Session(bind=engine, autoflush=False)

def get_data():
    Messages = ses.query(Message).filter(Message.status == 0).order_by(asc(Message.id)).all()
    if len(Messages)>0:
        return Messages[0]
    else:
        return False
def update_messag(messag,status):
    messag.status = status
    messag.datatime = datetime.now()
    ses.add(messag)
    ses.commit()
    return

