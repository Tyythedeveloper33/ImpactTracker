from datetime import datetime, timezone
from app.Models import db

class User(db.Model):
    __tablename__ = 'users'  # Explicitly set the table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    # Make sure the default is timezone-aware
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    donations = db.relationship('Donation', backref='user', lazy='joined')
    subscriptions = db.relationship('Subscription', backref='user', lazy='joined')

    def __repr__(self):
        return f"<User {self.username}>"
