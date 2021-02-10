from flask_sqlalchemy import SQLAlchemy 
db=SQLAlchemydef connect_db(app):
    """Connect to database"""
    db.app=app
    db.init_app(app)
    