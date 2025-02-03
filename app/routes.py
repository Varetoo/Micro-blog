from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Alvaro"}
    posts = [
        {
            "author": {"username":"Paco"},
            "body": "Bonito día el de hoy!!"
        },
        {
            "author": {"username":"Pepe"},
            "body": "Me siento genial!!"
        },
        {
            "author": {"username":"Juan"},
            "body": "Estoy muy cansado!!"
        }
    ]
    return render_template("index.html", title="Home page", user=user, posts=posts)
