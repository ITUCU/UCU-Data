from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(16), index = True, unique = True)
    email = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(16))
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    photo = db.Column(db.String(64))
    gender = db.Column(db.SmallInteger)
    role = db.Column(db.SmallInteger, default = 0)


    def __repr__(self):
        return '<User %r>' % (self.nickname)
