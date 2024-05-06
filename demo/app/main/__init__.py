from flask import Blueprint

# Creates a blueprint for all our code under main
main = Blueprint('main', __name__)

from . import views
