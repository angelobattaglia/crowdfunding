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

# Import the datetime library to handle the pubblication date of the posts
import datetime

## Import the dao modules and the models module
# importing get_all_posts() from post_dao.py, using it in home()
# import post_dao
# from post_dao import get_all_posts
# from post_dao import add_post
# # from post_dao import populate_posts_table
# import models
# import utenti_dao
# import commenti_dao
# from commenti_dao import add_comment
# from commenti_dao import get_comments

PROFILE_IMG_HEIGHT = 130
POST_IMG_WIDTH = 300

# create the application
app = Flask(__name__)
