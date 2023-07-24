from fastapi import APIRouter
from pydantic import BaseModel,Field
import  datetime
from sqlalchemy import  create_engine
from sqlalchemy.orm import Session,sessionmaker
from model import Message
import random


engine = create_engine('sqlite:///MassEmail.db', connect_args={'check_same_thread': False})
ses = Session(bind=engine, autoflush=False)

novelroute = APIRouter()
class messag_param(BaseModel):
    to: list = Field(
        description="Список получателей")

    subject: str = Field(
        description="Тема письма")

    message: str = Field(
        description="Сообщение")

    type : str = Field(
        description="Метод отправки")

    system: str = Field(
        description="Система отправления")

class out(BaseModel):
    err: str = Field("",
        description="Ошибка")
    messag_states: bool =Field(True,
        description="Состояние записи в очередь")
@novelroute.post('insert-messag', response_model=out, tags=["Заптсь сообщения в очередь"])
async def insert_message(param:messag_param):

    result = out()
    try:
        ses = Session(bind=engine, autoflush=False)
        for recipient in  param.to:
            New_message = Message()
            New_message.to = recipient
            New_message.subject=param.subject
            New_message.message=param.message
            New_message.type =param.type
            New_message.status = 0
            New_message.system =param.system
            ses.add(New_message)
        ses.commit()
        return result.__dict__
    except Exception as e:
        result.err = e
        result.messag_states = False
        return result.__dict__
