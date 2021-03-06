from flask import Flask
from config import DevConfig
import os
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE


from config import config_options

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

simple = SimpleMDE()


bootstrap = Bootstrap()
db = SQLAlchemy()

photos = UploadSet('photos',IMAGES)

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)

    mail.init_app(app)
    simple.init_app(app)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # configure UploadSet
    configure_uploads(app,photos)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # Will add the views and forms

        # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)



    return app
    

# Initializing application
app = Flask(__name__,instance_relative_config = True)
app.config["MOVIE_API_KEY"]=os.environ.get("MOVIE_API_KEY")
#app.config["MOVIE_API_BASE_URL"]=DevConfig.MOVIE_API_BASE_URL

# Setting up configuration
app.config.from_object(DevConfig)
#app.config.from_pyfile('config.py')


# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app.main import error
from app.main import views
# from app.main import error

  
