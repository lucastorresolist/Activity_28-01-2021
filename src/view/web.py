import sys
sys.path.append('.')

from flask import Flask, render_template, Blueprint, redirect

from src.view.category_view import category_bp

app = Flask(__name__)
app.register_blueprint(category_bp)

@app.route("/")
def index():
    return redirect('/category')

app.run(debug=True)
