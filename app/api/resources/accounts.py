from flask_restful import Resource


class User(Resource):
    def get(self):
        return {'foo': 'bar'}

    def post(self):
        return None

    def patch(self):
        return None


class Users(Resource):
    def get(self):
        return None
