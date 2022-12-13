from usedcar_app import db

class Member(db.Model):
    __tablename__ = "MEMBER_TB"
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    nickname = db.Column(db.String(200), nullable=True)