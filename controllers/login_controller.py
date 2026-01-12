from flask import render_template, request,redirect,session;
from models.login import CheckLogin
from flask_session import Session;
class LoginController:
   def index(self):
      poruka=''
      if( request.method == 'POST' ):
          session['username']=request.form.get('ime')
          session['password']=request.form.get('lozinka')
          user = CheckLogin.check_login( session['username'],session['password']);

          if(user):
             print("Unosim usera u flask login")
             print("i nije bacio gresku")
             return redirect('/svidogadaji')
          else:
             poruka="Niste unijeli točno ime ili lozinku."

      return render_template('login.html',poruka=poruka)
      

