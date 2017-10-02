#!/usr/bin/python3
"""
creating a Blueprint instance
"""
from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.users import *

"""
creating blueprint instance
"""
app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")
