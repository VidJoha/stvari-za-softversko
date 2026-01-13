from models.models import db as sqlalchemy_db
from models.user import User

class CheckMail:
    def check_mail(username):
        db = get_db_connection();
        cursor = db.cursor();
        sqlalchemy_db.session.execute( sqlalchemy_db.select(User).where(User.username == username) ).update({"has_registered": 1})
