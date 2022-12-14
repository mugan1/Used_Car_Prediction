from usedcar_app import db

class Input(db.Model):
    __tablename__ = 'input'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    km = db.Column(db.Integer, nullable=False)
    fuel = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    ratio = db.Column(db.Float, nullable=False)
    drive = db.Column(db.Integer, nullable=False)
    torque = db.Column(db.Float, nullable=False)
    insurance = db.Column(db.Integer, nullable=False)
    factory = db.Column(db.Integer, nullable=False)
    horse = db.Column(db.Float, nullable=False)
    guarantee = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"Input {self.id}"