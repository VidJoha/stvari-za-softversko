from werkzeug.security import check_password_hash
import importlib;
from models.models import db as sqlalchemy_db
from models.user import User

class NewRegister:
    def new_register(username,password,email):

        user = sqlalchemy_db.session.execute( sqlalchemy_db.select(User).where(User.username == username) ).scalars().one()
        if(user is not None):
            return None
        #TODO Završit ubacijvanje podataka u bazu i slanje maila

class User2:
    def __init__(this, id, username):
        # Obično želimo usere identificirati preko id-a umjesto username-a.
        this.id = id;
        this.username = username;

