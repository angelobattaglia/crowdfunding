from flask_login import UserMixin

"""
When you write class " User(UserMixin): ", you're telling Python to
create a new class called User that inherits from UserMixin. This means
the User class will automatically include all the methods and properties
defined in UserMixin, such as is_authenticated, is_active, is_anonymous,
and get_id(), which are required by Flask-Login to manage user sessions
and authentication.

By inheriting from UserMixin, the User class becomes compatible with Flask-Login's
requirements, allowing Flask-Login to use instances of the User class to represent
and manage logged-in users in a Flask application.

e.g.:
user = User(id=1, nickname='john_doe', password='hashed_password_here', 
                immagine_profilo='path/to/profile_pic.jpg')

"""
class User(UserMixin):
    def __init__(self, id, nickname, email, password):
        self.id = id
        self.nickname = nickname
        self.email = email
        self.password = password
