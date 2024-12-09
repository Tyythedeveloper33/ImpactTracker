# this route is going to import all of the clases
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


from app.Models.User import User
from app.Models.Donation import Donation
from app.Models.Statement import Statement
