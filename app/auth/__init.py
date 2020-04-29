from flask import Blueprint
from app.auth import views,forms

auth = Blueprint('auth',__name__)

from app.auth import views
