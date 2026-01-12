from werkzeug.security import check_password_hash
import importlib;
from models.models import db as sqlalchemy_db
from models.user import User

class CheckLogin:
    def check_login( username, password ):
        # Provjeri postoji li korisnik s ovim username-om i passwordom.
        
        user = sqlalchemy_db.session.execute( sqlalchemy_db.select(User).where(User.username == username) ).scalars().one()
        user2=User2(user.id_user,user.username,user.password_hash)
        if(check_password_hash(user2.password,password)):
            return user2

        return None;

class User2:
    def __init__(this, id, username, password):
        # Obično želimo usere identificirati preko id-a umjesto username-a.
        this.id = id;
        this.username = username;
        this.password = password;
