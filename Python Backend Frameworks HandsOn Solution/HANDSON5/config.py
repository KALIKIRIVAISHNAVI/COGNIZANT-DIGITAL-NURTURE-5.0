import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this-secret'
    # Creates courses.db right inside your project directory
    SQLALCHEMY_DATABASE_URI = 'sqlite:///courses.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True