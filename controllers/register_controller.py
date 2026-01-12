from flask import render_template, request,redirect,session;
from models.register import NewRegister;
from flask_session import Session;
class RegisterController:
   def index(self):
      poruka=''
      if( request.method == 'POST' ):
          session['username']=request.form.get('ime')
          session['password']=request.form.get('lozinka')
          session['email']=request.form.get('email')
          
          user = CheckLogin.new_register(session['username'],session['password'],session['email']);

          if(user):
             return redirect('/svidogadaji')
          else:
             poruka="To ime je već zauzeto"

      return render_template('login.html',poruka=poruka)
      
