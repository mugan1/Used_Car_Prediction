from usedcar_app import db

class Car(db.Model):
    __tablename__ = 'car'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    km = db.Column(db.Integer, nullable=False)
    fuel = db.Column(db.String(64), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    ratio = db.Column(db.Float, nullable=False)
    drive = db.Column(db.String(64), nullable=False)
    torque = db.Column(db.Float, nullable=False)
    insurance = db.Column(db.String(64), nullable=False)
    factory = db.Column(db.String(64), nullable=False)
    horse = db.Column(db.Float, nullable=False)
    guarantee = db.Column(db.Float, nullable=False)

    def __init__(self, name, price, year, km, fuel, amount, ratio, drive, torque, insurance, factory, horse, guarantee):

        self.name= name
        self.price = price
        self.year = year
        self.km = km
        self.fuel = fuel
        self.amount = amount 
        self.ratio = ratio 
        self.drive = drive 
        self.torque = torque 
        self.insurance = insurance 
        self.factory = factory 
        self.horse = horse 
        self.guarantee = guarantee 

    def __repr__(self):
        return f"Car {self.id}"