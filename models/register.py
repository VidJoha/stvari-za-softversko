from werkzeug.security import check_password_hash,generate_password_hash;
import importlib;
from flask import Flask,g, current_app;
import pymysql;
from models.models import db as sqlalchemy_db
from models.user import User
from flask_mail import Mail,Message;
import random;
import string;
app = Flask( __name__ );
mail=Mail(app);
class NewRegister:
    def new_register(username,password,email):
        print("Postoji li taj korisnik???")
        users = sqlalchemy_db.session.execute( sqlalchemy_db.select(User).where(User.username == username) ).scalars()
        for user in users:
            if(user.username==username):
                return 0

        print("Ne postoji")
        length=20;
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length));

        print("Spajanje na bazu")
        db = get_db_connection();
        cursor = db.cursor();
        print("Spojen na bazu")
        sql = 'INSERT INTO users(username, password_hash, email, registration_sequence, has_registered) VALUES (%(username)s, %(password)s, %(email)s, %(regseq)s, \'0\')';
        cursor.execute( sql,
        {'username': username, 'password': generate_password_hash( password ),'email': email,'regseq':random_string} );
        print("Dodan lik")
        msg=Message(
            subject='Poruka poslana iz Flaska',
            recipients=[email],
            body='http://127.0.0.1:5000/mail',
        );
        print("Napisan mail")
        mail.send(msg);#TU JE PROBLEM KOJI NE ZNAM RJEŠIT KAŽE ERROR 111 CONNECTION REFUSED
        print("Poslan mail")
        return redirect('/login');

class User2:
    def __init__(this, id, username):
        # Obično želimo usere identificirati preko id-a umjesto username-a.
        this.id = id;
        this.username = username;

def get_db_connection():
    if( 'db_connection' not in g ):
        g.db_connection = pymysql.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASS'],
            database=current_app.config['DATABASE_DB'],
            cursorclass=pymysql.cursors.DictCursor
        );

    return g.db_connection;
