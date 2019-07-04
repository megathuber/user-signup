from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True     

@app.route("/", methods=['POST', 'GET'])
def index(): 
    return render_template('signup.html')

@app.route('/validate_signup', methods=['POST', 'GET'])
def validate_signup():  
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email'] 

    un_error = ''
    pw_error = ''
    vpw_error = ''
    email_error = ''
#username verification:
    if (not username) or (username.strip() == ""):
        un_error = 'Please specify a username'
    
    if len(username) < 3 or len(username) > 20:
        un_error = 'Username out of range (3-20 characters)'
    
    if ' ' in username:
        un_error = 'Username cannot have spaces'
#password verification:        
    if (not password) or (password.strip() == ""):
        pw_error = 'Please specify a password'
        password = ''
    
    if len(password) > 0 and len(password) < 3 or len(password) > 20:
        pw_error = 'Password out of range (3-20 characters)'
        password = ''
    
    if ' ' in password:
        pw_error = 'Passowrd cannot have spaces'
        password = ''
#verify password error:
    if (not vpassword) or (vpassword.strip() == ""):
        vpw_error = 'Please verify your password'
        vpassword = ''
    
    if password != vpassword:
        vpw_error = 'Verification password does not match'
        vpassword = ''
#email verification:
    if len(email) > 0:
        if ' ' in email or len(email)>20 or len(email)<3 or email.count("@")!=1 or email.count(".")!=1:
            email_error = 'Please enter a valid email'
        
    if not un_error and not pw_error and not vpw_error and not email_error:
        return redirect('/welcome_page?username={0}'.format(username))
    else:
        return render_template('signup.html', 
            username=username, un_error=un_error,
            password=password, pw_error=pw_error,
            vpassword=vpassword, vpw_error=vpw_error,
            email=email, email_error=email_error)   

@app.route('/welcome_page', methods=['POST', 'GET'])
def welcome_page():
    username = request.args.get('username')
    return render_template('welcome_page.html', username=username)

app.run()



