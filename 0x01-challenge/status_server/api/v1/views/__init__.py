#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint
from .status import status_bp

app_views = Blueprint("app_views", __name__)
app_views.register_blueprint(status_bp)

from api.v1.views.index import *
