from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from flask_redis import FlaskRedis


# Globally accessible libraries
#db = SQLAlchemy()
#r = FlaskRedis()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    #db.init_app(app)
    #r.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes

        
        return app