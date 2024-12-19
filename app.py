from flask import Flask
from routes.books import books_bp
from routes.members import members_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(books_bp)
app.register_blueprint(members_bp)

if __name__ == "__main__":
    app.run(debug=True)
