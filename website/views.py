from flask import Blueprint, render_template
from .models import Entry_info

views = Blueprint("views",__name__)

@staticmethod
@views.route("/")
def entry():
    entry_info = Entry_info()
    return render_template("entry.html", site_name=entry_info.site_name)





