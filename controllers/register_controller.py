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
          
          user = NewRegister.new_register(session['username'],session['password'],session['email']);

          if(user==0):
             poruka="To ime je već zauzeto"
          else:
             return redirect('/svidogadaji')

      return render_template('login.html',poruka=poruka)

      
