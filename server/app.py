from flask import Flask, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///apartments.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

migrate = Migrate( app, db )
db.init_app( app )

@app.route("")

if __name__ == '__main__':
    app.run( port = 3000, debug = True )