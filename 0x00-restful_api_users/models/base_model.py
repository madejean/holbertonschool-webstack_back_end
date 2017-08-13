#!/usr/bin/python3
"""
    BaseModel
"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel():
    """
        Creating BaseModel class/ parent of all future models
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow()
    )

    def __init__(self):
        """
            override the instance creation method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @classmethod
    def all(cls):
        """returns all instances of cls from MySQL database"""
        from models import db_session
        return db_session.query(cls).order_by(cls.created_at).all()

    @classmethod
    def count(cls):
        """returns the number instances of cls objects in MySQL database"""
        from models import db_session
        return db_session.query(cls).count()

    @classmethod
    def first(cls):
        """returns all instances of cls from MySQL database"""
        from models import db_session
        return db_session.query(cls).order_by(cls.created_at).first()
