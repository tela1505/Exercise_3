from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os.path import dirname, abspath, join

#from config import DevConfig

# The SQLAlchemy object is defined globally
db = SQLAlchemy()


def page_not_found(e):
    return render_template('404.html'), 404


def internal_server_error(e):
    return render_template('500.html'), 500

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dfdQbTOExternjy5xmCNaA'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CWD = dirname(abspath(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(CWD, 'rain.db')
    db.init_app(app)
    # The following is needed if you want to map classes to an existing database
    #with app.app_context():
    #    db.Model.metadata.reflect(db.engine)
    # If you don't have a database with records that you created in ex1 then you all need to create the database tables by uncommenting the following lines
    from app.models import User, Forecast, City
    with app.app_context():
        db.create_all()


    # Register error handlers
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app
