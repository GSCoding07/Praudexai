from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/')
def entry():
    return render_template("entry.html")

