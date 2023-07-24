from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey,DateTime,Boolean,DATETIME
from sqlalchemy.orm import registry


metadata = MetaData()
mapper_registry = registry()

message = Table('message', metadata,
    Column('id', Integer(), primary_key=True),
    Column("to", String(200), nullable=False),
    Column("subject", String(200),  nullable=False),
    Column("message", Text(),  nullable=False),
    Column("type", String(200),  nullable=False),
    Column("status", Integer(),  nullable=False),
    Column("system", String(200),  nullable=False),
    Column("datatime", DATETIME(), nullable=False))

user = Table("User", metadata,
	Column("id", Integer(), primary_key=True, nullable=False),
	Column("name", String(64), unique=True, index=True, nullable=False),
	Column("username", String(64), unique=True, index=True, nullable=False),
	Column("email", String(64) ,nullable=False),
	Column("password", String(128), nullable=False))

class Message(object):
    pass

class User(object):
    pass

mapper_registry.map_imperatively(Message, message)
mapper_registry.map_imperatively(User, user)