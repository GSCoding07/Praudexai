from flask import Blueprint, render_template

views = Blueprint("views",__name__)

site_name = "Praudexai"

@staticmethod
@views.route("/")
def entry():
    return render_template("entry.html", site_name = site_name)



