from flask import Flask
from .config import DevConfig
from app.instance.config import MOVIE_API_KEY
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__,instance_relative_config = True)
app.config["MOVIE_API_KEY"]=MOVIE_API_KEY
#app.config["MOVIE_API_BASE_URL"]=DevConfig.MOVIE_API_BASE_URL

# Setting up configuration
app.config.from_object(DevConfig)
#app.config.from_pyfile('config.py')


# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
from app import error

