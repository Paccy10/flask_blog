import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app import app

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
