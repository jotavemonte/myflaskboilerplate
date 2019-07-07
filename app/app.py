# flake8: noqa
from flask_bcrypt import Bcrypt

from . import create_app
from .api import api_bp


app = create_app()
bcrypt = Bcrypt(app)


app.register_blueprint(api_bp, url_prefix='/api')

# register models
from app.api.models import *