from ..util.Database import db


class DailyReport(db.Model):
    """ User Model for storing covid-19 daily reports """
    __tablename__ = "daily_reports"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(100))
    report_date = db.Column(db.Date())
    total_confirmed = db.Column(db.Integer())
    total_deaths = db.Column(db.Integer())
    total_recovered = db.Column(db.Integer())
    total_active = db.Column(db.Integer())

    new_confirmed = db.Column(db.Integer())
    new_deaths = db.Column(db.Integer())
    new_recovered = db.Column(db.Integer())
    death_rate = db.Column(db.Float())
    increase_rate = db.Column(db.Float())

    def serialize(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
