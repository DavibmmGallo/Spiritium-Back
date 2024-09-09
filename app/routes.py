from flask import Flask, jsonify, request
from flask_cors import CORS
from .models import User, Article
from dataclasses import asdict
from db import get_database
from flask_jwt_extended import create_access_token, JWTManager
from http import HTTPStatus
import secrets
from datetime import timedelta, datetime

def create_server(config):
    '''Starts flask server'''
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(32)
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=60)

    CORS(app)
    JWTManager(app)

    db = get_database(config.MONGO_SETTINGS)
    
    @app.post("/users")
    def postUser():
        data = request.json
        user = User.new(data)
        db.get_collection("users").insert_one(asdict(user))

        return jsonify(user), HTTPStatus.CREATED
 
    @app.get("/users/<string:id>")
    def getUser(id):
        user = db.get_collection("users").find_one({"_id": id})

        return jsonify(user), HTTPStatus.ACCEPTED

    @app.post("/users/<string:email>")
    def login(email):
        data = dict(request.json)
        user = dict(db.get_collection("users").find_one({"email": email}))
        if user.get('password') == data.get('password'):
            access_token = create_access_token(identity=email, additional_claims={"id": user.get('id'), "name": user.get('name')})
            return jsonify({"access_token": access_token}), HTTPStatus.ACCEPTED

        return jsonify({'msg': f'The password for {email} is incorrect.'}), HTTPStatus.UNAUTHORIZED 

    @app.post("/articles")
    def postArticle():
        data = request.json
        del data['_id']
        data['release_date'] = datetime.now()
        article = Article.new(data)
        db.get_collection("articles").insert_one(asdict(article))

        return jsonify(article), HTTPStatus.CREATED
 
    @app.get("/articles")
    def getArticles():
        articles = list(db.get_collection("articles").find())

        return jsonify(articles), HTTPStatus.ACCEPTED

    @app.get("/articles/<string:id>")
    def getArticle(id):
        article = db.get_collection("articles").find_one({"_id": id})

        return jsonify(article), HTTPStatus.ACCEPTED
    

    return app