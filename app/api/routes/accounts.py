from app.api import api
from app.api.resources.accounts import User, Users

api.add_resource(User, '/user')
api.add_resource(Users, '/users')
