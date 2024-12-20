from flask import Flask
from extensions import db, migrate
import psycopg2
import os
from flask_jwt_extended import JWTManager
from auth import auth_bp
from flask_cors import CORS 
from models.user import User 

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'ae4fd98e444bd859f1947549d53531d8f084fd84bd2ee5b95f438572a4bc5c9e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/farmer'

CORS(app)
db.init_app(app)
migrate.init_app(app, db)
jwt = JWTManager(app)

def register_blueprints(app):
    from views.user_view import user_blueprint
    from views.country_view import country_blueprint
    from views.schedule_view import schedule_blueprint
    from views.farm_view import farm_blueprint
    from views.farmer_view import farmer_blueprint
    from auth import auth_bp

    app.register_blueprint(country_blueprint, url_prefix='/country')
    app.register_blueprint(farm_blueprint, url_prefix='/farm')
    app.register_blueprint(farmer_blueprint, url_prefix='/farmer')
    app.register_blueprint(schedule_blueprint, url_prefix='/schedule')
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(auth_bp,url_prefix='/auth')  

register_blueprints(app)


# Seed database with initial data
def seed_database():
    if not User.query.filter_by(username='superadmin').first():
        superadmin = User(username='superadmin')
        superadmin.set_password('superadmin_password')
        superadmin.roles = ['superadmin']
        db.session.add(superadmin)
        print("SUPERADMIN created.")

    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin')
        admin.set_password('admin_password')
        admin.roles = ['admin']
        db.session.add(admin)
        print("ADMIN created.")

    if not User.query.filter_by(username='viewer').first():
        viewer = User(username='viewer')
        viewer.set_password('viewer_password')
        viewer.roles = ['viewer']
        db.session.add(viewer)
        print("VIEWER created.")

    db.session.commit()

# Run seed logic before the first request
@app.before_first_request
def setup():
    with app.app_context():
        db.create_all()  
        seed_database() 


# Connect to PostgreSQL using environment variable
def get_db_connection():                          # responsible for establishing a connection to the PostgreSQL database
    database_url = os.getenv('SQLALCHEMY_DATABASE_URI')      # get DATABASE_URL from environment
    print(database_url)
    breakpoint()
    conn = psycopg2.connect(database_url)
    return conn



@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT NOW();')                # Run a simple query to check DB connection
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return f'Database connected Shashank Mishra! Current time: {result[0]}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)



# app.py is the generic entry point for Abseil Python applications(the main application file for the project). 
# This is a key difference from how python applications are typically run, where you identify a specific file as the entry point, e.g., $ python my_app.py .

# psycopg2 library is used to connect and interact with PostgreSQL databases in Python
# os module to access environment variables.
# app = Flask(__name__) - This initializes the Flask application object (app), this object is used to define routes and configuration for the web app.

# It retrieves the database URL from an environment variable DATABASE_URL using os.getenv(). 
# This URL contains the connection string for the PostgreSQL database.
# It then uses psycopg2.connect() to establish the connection to the database.
# The connection object (conn) is returned.

# This block ensures that the Flask application runs when the script is executed directly (not imported as a module).
# app.run(debug=True, host='0.0.0.0'): Starts the Flask development server with debugging enabled 
# (debug=True), and binds it to all available network interfaces (host='0.0.0.0'), making the app accessible from any IP address.

# This Flask application serves as a backend server that connects to a PostgreSQL database and uses Flask extensions like flask_jwt_extended for JWT authentication and Flask-Migrate for database migrations.



