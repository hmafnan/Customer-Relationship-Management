from datetime import datetime
from crm import db

class Lead(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(50))
    company = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True)
    touches = db.relationship('Touch', backref='author')

    def __repr__(self):
        return "Lead({})".format(self.name)


class Touch(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    description = db.Column(db.Text)
    date = db.Column(db.DATETIME, nullable=False, default=datetime.utcnow)
    lead_id = db.Column(db.INTEGER, db.ForeignKey('lead.id'), nullable=False)

    def __repr__(self):

        return "Touch({}, {})".format(self.description[0:20], self.date)