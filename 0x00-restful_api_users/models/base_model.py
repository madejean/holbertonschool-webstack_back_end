#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel(object):
    id = None
    created_at = None
    updated_at = None

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
