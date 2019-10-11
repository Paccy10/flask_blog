from app import app
from routes.main import main
from routes.user import users
from routes.post import posts
from routes.errors import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)


if __name__ == '__main__':
    app.run(debug=True)
