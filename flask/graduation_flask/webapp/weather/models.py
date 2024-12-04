from webapp import db

associations = db.Table('associations',
                        db.Column('city_id', db.Integer, db.ForeignKey('cities.id')),
                        db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
                        )


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    users = db.relationship('User', secondary=associations, backref='cities')

    def __str__(self):
        return self.name