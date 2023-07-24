from sqlalchemy import  create_engine,desc
from sqlalchemy.orm import Session,sessionmaker
from model import Message,User


engine = create_engine('sqlite:///MassEmail.db', connect_args={'check_same_thread': False})
ses = Session(bind=engine, autoflush=False)

def get_data():
    Messages = ses.query(Message).order_by(desc(Message.id)).limit(10000)
    return Messages

def get_count():
    count_sent= ses.query(Message).filter( Message.status == 1).count()
    count_error= ses.query(Message).filter( Message.status == -1).count()
    count_queue= ses.query(Message).filter( Message.status == 0).count()
    return [{'count_sent':count_sent,'count_error':count_error,'count_queue':count_queue}]

def get_users():
    Users = ses.query(User).all()
    Users_data = {"usernames":""}

    for user in Users:
        Users_data["usernames"] = {user.username:
                       {"email": user.email,
                        "name": user.name,
                        "password": user.password}}

    return Users_data