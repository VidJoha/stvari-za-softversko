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

          if(user==0):
             poruka="Provjerite mail."
          elif(user==1):
             poruka="Niste unijeli točno ime ili lozinku."
          else:
             return redirect('/svidogadaji')

      return render_template('login.html',poruka=poruka)
      

