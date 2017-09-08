#!/usr/bin/python3
"""
creating a Blueprint instance
"""
from api.v1.views.index import *
from api.v1.views.users import *

from flask import Blueprint, render_template

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")
