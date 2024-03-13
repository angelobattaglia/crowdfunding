# Note: it is important to add "render_template" to the imports
from flask import Flask, render_template
from flask import Flask, render_template, request
from flask import redirect, url_for, flash, abort

# Flask-Login is a Flask extension that provides a framework for handling user authentication
import flask_login
from flask_login import LoginManager
from flask_login import login_required
# Logs a user in. We should pass the actual user object to this method:
# returns True if the log in attempt succeeds, and False if it fails
from flask_login import login_user

# Security and Forms for the login
import werkzeug.security as ws
# from forms import LoginForm

# Import the Image module from the PIL (Python Imaging Library) package. 
# Used to preprocess the images uploaded by the users. 
# Ensure 'Pillow' is installed before running the application by using
# the command 'pip install Pillow'
from PIL import Image
PROFILE_IMG_HEIGHT = 130
POST_IMG_WIDTH = 300

# Import the datetime library to handle the pubblication date of the raccolte
import datetime

## Import the dao modules and the models module
import models
import utenti_dao
import raccolte_dao

# create the application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'gematria'

# This is for login_manager 
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    # I collect all the users and the raccolte
    raccolte = []
    users = []
    raccolte = raccolte_dao.get_raccolte()
    users = utenti_dao.get_users()

    # I create a new dictionary of raccolte with the nickname of the user as the last field
    raccolte_new = []
    for raccolta in raccolte:
        for user in users:
            if raccolta['id_utente'] == user['id']:
                # first I have to convert the string to a datetime object, so that I can compare it using Jinja
                end_time_dt_obj = datetime.datetime.strptime(raccolta["EndTime"], "%Y-%m-%d %H:%M:%S.%f")
                # Then I define these new fields
                raccolta['end_time_dt_obj'] = end_time_dt_obj
                raccolta['nickname'] = user['nickname']
                # Filter only active raccolte
                if  end_time_dt_obj > datetime.datetime.now():
                    raccolte_new.append(raccolta)
    
    
    # I get the current time and pass it along
    current_time=datetime.datetime.now()
        
    # Passing the current time, so that if the time's up, it displays it
    # I pass the raccolte_new to the home.html template
    return render_template('home.html', raccolte_new = raccolte_new, current_time=current_time, title='Home')


@app.route('/raccolte-chiuse')
def raccolte_chiuse():
    # I collect all the users and the raccolte
    raccolte = []
    users = []
    raccolte = raccolte_dao.get_raccolte()
    users = utenti_dao.get_users()

    # I create a new dictionary of raccolte with the nickname of the user as the last field
    raccolte_new = []
    for raccolta in raccolte:
        for user in users:
            if raccolta['id_utente'] == user['id']:
                # first I have to convert the string to a datetime object, so that I can compare it using Jinja
                end_time_dt_obj = datetime.datetime.strptime(raccolta["EndTime"], "%Y-%m-%d %H:%M:%S.%f")
                # Then I define these new fields
                raccolta['end_time_dt_obj'] = end_time_dt_obj
                raccolta['nickname'] = user['nickname']
                # Filter only inactive raccolte
                if  end_time_dt_obj <= datetime.datetime.now():
                    raccolte_new.append(raccolta)    
    
    # I get the current time and pass it along
    current_time=datetime.datetime.now()
        
    # Passing the current time, so that if the time's up, it displays it
    # I pass the raccolte_new to the home.html template
    return render_template('home.html', raccolte_new = raccolte_new, current_time=current_time, title='Home')

#########################################################
#########################################################
#########################################################
###########Poi si fa il post (raccolta)##################
#########################################################
#########################################################
#########################################################
#########################################################


@app.route('/new_raccolta', methods=['GET', 'POST'])
@login_required
def new_raccolta():

    raccolta = request.form.to_dict()

    # I make some checks and analysis on the raccolta dictionary

    #### Here's the values I'm passing from the form:
    
    #-----------------------------------------------------------------------
    ### Time-related values
    ## raccolta['collection_type'] # This is the type of the collection
    ## raccolta['end_time'] # This is the end time of the collection
    ## raccolta['date'] # this is the date of the collection
    # if datetime.datetime.strptime(raccolta['StartTime'], '%Y-%m-%d').date() < datetime.date.today():
        # app.logger.error('Data errata')
        # return redirect(url_for('home'))

    
    #-----------------------------------------------------------------------
    ### Donation-related values
    ## raccolta['minDonation'] # This is the minimum amount of the collections
    ## raccolta['maxDonation'] # This is the maximum amount of the collections
    ## raccolta['donationTarget'] # This is the target amount of the collection

    if raccolta['collectionType'] == 'flash':
        # Set the duration to 5 minutes from now
        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
        raccolta['StartTime'] = start_time
        raccolta['EndTime'] = end_time
        # Process the flash collection here
    elif raccolta['collectionType'] == 'fourteenDay':
        # Set the duration to 14 days from now
        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now() + datetime.timedelta(days=14)
        raccolta['StartTime'] = start_time
        raccolta['EndTime'] = end_time
        # Process the 14-day collection here
    elif raccolta['collectionType'] == '':
        app.logger.error('Devi selezionare una collection_type!')
        return redirect(url_for('home'))

    #----------------------------------------------------------------------
    ### Post-related values
    ## raccolta['nome_raccolta'] # This is the name of the collection
    ## raccolta['text'] # This is the reason of the collection
    ## raccolta['immagine_raccolta'] # This is the image of the collection

    # If the raccolta is either empty, with a wrong date or with a date
    # corresponding to a day that has already passed, you get redirected to
    # the home page and an error message is logged
    if raccolta['nome_raccolta'] == '':
        app.logger.error('Il nome della raccolta non può essere vuoto!')
        return redirect(url_for('home'))
    if raccolta['text'] == '':
        app.logger.error('Il post non può essere vuoto!')
        return redirect(url_for('home'))

    post_image = request.files['immagine_raccolta']
    if post_image:

        # Open the user-provided image using the Image module
        img = Image.open(post_image)

        # Get the width and height of the image
        width, height = img.size

        # Calculate the new height while maintaining the aspect ratio based on the desired width
        new_height = height/width * POST_IMG_WIDTH

        # Define the size for thumbnail creation with the desired width and calculated height
        size = POST_IMG_WIDTH, new_height
        img.thumbnail(size, Image.Resampling.LANCZOS)

        # Extracting file extension from the image filename
        ext = post_image.filename.split('.')[-1]
        # Getting the current timestamp in seconds
        secondi = int(datetime.datetime.now().timestamp())       

        # Saving the image with a unique filename in the 'static' directory
        img.save('static/@' + flask_login.current_user.nickname.lower() + '-' + str(secondi) + '.' + ext)

        # Updating the 'immagine_post' field in the post dictionary with the image filename
        raccolta['immagine_raccolta'] = '@' + flask_login.current_user.nickname.lower() + '-' + str(secondi) + '.' + ext

    #-----------------------------------------------------------------------
    ### Utente-related values
    ## raccolta['id_utente'] # This is the id of the user
    ## raccolta['nickname'] # This is the nickname of the user
    raccolta['id_utente'] = int(flask_login.current_user.id)  # flask_login.current_user.id is the id of the current user
    # I'm not sure if the following line is needed
    # raccolta['nickname'] = str(flask_login.current_user.nickname)

    #-----------------------------------------------------------------------
    # After finishing making the checks, I put the "post" dictionary in the database
    success = raccolte_dao.add_raccolta(raccolta)

    if success:
        app.logger.info('Post creato correttamente')
    else:
        app.logger.error('Errore nella creazione del post: riprova!')

    return redirect(url_for('home'))

# Dynamic routing
@app.route('/raccolta/<int:raccolta_id>')
def raccolta(raccolta_id):
    raccolte = []
    raccolte = raccolte_dao.get_all_raccolte()
    
    # Check if the provided raccolta_id is within the valid range
    if raccolta_id < 0 or raccolta_id > len(raccolte):
        abort(403)  # Post not found, return a 404 error

    raccolta = raccolte[raccolta_id-1]
    # raccolta = raccolte[raccolta_id-2]

    # I also have to pass him the user to whom the post belongs, 
    # each post has a user_id field, so I use post_dao's get_user_by_id method ..
    usr = utenti_dao.get_user_by_id(raccolta['id_utente'])
    # # I should implement the following
    # current_time = datetime.datetime.now()

    # Donations for the post with post_id equal to the one passed in the URL
    # donations = donazioni_dao.get_donazioni(raccolta_id)

    return render_template('raccolta.html', raccolta = raccolta, usr = usr, title='Raccolta')

# Deleting a raccolta
@app.route('/delete_raccolta/<int:id>', methods=['POST'])
@login_required
def delete_raccolta_route(id):
    # Authenticate: Check if the current_user's ID matches the ID of the user who created the raccolta
    # This part depends on how you associate raccolte with users in your database
    # For demonstration, let's assume you have a function get_raccolta_creator_id that returns the creator's ID given a raccolta ID
    raccolta = raccolte_dao.get_raccolta(id)
    creator_id = utenti_dao.get_user_by_id(raccolta['id'])
    raccolta = raccolte_dao.get_raccolta(id)
    

    # Ensure that your deletion route (/delete_raccolta/<int:id>) is secure, especially since it's using a POST method. 
    # The check to ensure that the current user is the creator of the raccolta before allowing deletion is good practice.
    # Authentication Check: Your route should verify that the user is authenticated before proceeding with any deletion logic. 
    # Flask-Login's current_user.is_authenticated is useful for this purpose, and you're already using @login_required to protect the route.
    # Authorization Check: It's essential to ensure that the authenticated user has the right to delete the specific raccolta. 
    # This involves checking that the current user is the creator of the raccolta or has sufficient permissions. 
    # Your approach of comparing the current user's ID with the creator's ID is a good practice for this authorization check.
    if flask_login.current_user.id != raccolta['id_utente']:
        flash('You are not authorized to delete this post.')
        return redirect(url_for('home'))

    if flask_login.current_user.id != creator_id:
        flash('You are not authorized to delete this post.')
        return redirect(url_for('home'))

    # Perform the deletion
    success = raccolte_dao.delete_raccolta(id)  # Assuming this is the function from your DAO file

    if success:
        flash('Post deleted successfully.')
    else:
        flash('An error occurred while trying to delete the post.')

    # Redirect after deletion
    return redirect(url_for('home'))


#########################################################
#########################################################
#########################################################
#######Prima si fa Il signup e il login##################
#########################################################
#########################################################
#########################################################
#########################################################

# Define the signup page
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup_function():

    # I take from the form the input datas and import them locally as a dictionary
    nuovo_utente_form = request.form.to_dict()

    # I try to retrieve the unique email of the nuovo_utente_form from the db ..
    user_in_db = utenti_dao.get_user_by_nickname(nuovo_utente_form.get('email'))

    # ... and I check weather it has already been registered ..
    if user_in_db:
        flash('There\'s already a user with these credentials', 'danger')
        return redirect(url_for('signup'))
    # .. and if it hasn't been registered ..
    else:
        # I generate an hash for the password that has been inserted by the form input
        nuovo_utente_form['password'] = ws.generate_password_hash(nuovo_utente_form.get('password'))

        # I add the user to the db using the method "add_user" from the utenti_dao.py
        success = utenti_dao.add_user(nuovo_utente_form)

        if success:
            flash('Utente creato correttamente', 'success')
            return redirect(url_for('home'))
        else:
            flash('Errore nella creazione del utente: riprova!', 'danger')
            return redirect(url_for('signup'))

@login_manager.user_loader
def load_user(user_id):
    db_user = utenti_dao.get_user_by_id(user_id)
    if db_user is not None:
        user = models.User(id=db_user['id'], 
                           nickname=db_user['nickname'],	
                           email=db_user['email'],
                           password=db_user['password'])
    else:
        user = None
    return user

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():

    # Retrieving the informations from the form @ /login
    utente_form = request.form.to_dict()
    # Using the "get_user_by_nickname" method from utenti.dao, which
    # retrieves the user from the database with the given nickname passed
    # from the form in /login
    utente_db = utenti_dao.get_user_by_email(utente_form['email'])

    # If there's no utente_db in the database (meaning the user just doesn't exist into the db)
    # or if the password given as input in the form /login isn't equal to the one in the database
    if not utente_db or not ws.check_password_hash(utente_db['password'], utente_form['password']):
        flash('Credenziali non valide, riprova', 'danger')
        return redirect(url_for('home'))
    else:
    # if, instead, it exists, we create a new user instance using the "User model" defined in models.py
        # Create a new user instance called "new"
        new = models.User(id=utente_db['id'], 
                          nickname=utente_db['nickname'], 
                          email=utente_db['email'],
                          password=utente_db['password'])
        # We log in said user called "new"
        flask_login.login_user(new, True)
        flash('Bentornato ' + utente_db['nickname'] + '!', 'success')
        return redirect(url_for('home'))

# Log out route
@app.route("/logout")
@login_required
def logout():
    flask_login.logout_user()
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')
