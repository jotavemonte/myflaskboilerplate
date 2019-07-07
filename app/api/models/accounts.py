from app import db
from app.app import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_superuser = db.Column(db.Bool(), default=False)
    is_superuser = db.Column(db.Bool(), default=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
