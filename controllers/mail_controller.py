from flask import Flask,session;
from flask_session import Session;
from flask_mail import Mail,Message;



class MailController:
    def index(self):
        username=session['username'];
        user=CheckMail.check_mail(username);

