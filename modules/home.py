# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify

home = Blueprint('home', __name__, template_folder='templates')


@home.route("/")
def index():
    return render_template("home.index.html")


@home.route('/hello/<name>')
def withdata(name):
    payload = {
        'nama_orang': name
    }

    return render_template("home.withdata.html", data=payload)


@home.route("/json")
def returnjson():

    return jsonify({
        "message": "this is from modules.home.returnjson",
        "code": 200
    })