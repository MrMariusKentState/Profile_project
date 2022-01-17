from flask import render_template, redirect

from flask_app import app


@app.route('/')
def home():
    return render_template ("index.html")


@app.route('/linkedin')
def linkedin():
    return redirect ("https://www.linkedin.com/in/mariuspaulikas/")

@app.route('/github')
def github():
    return redirect ("https://github.com/MrMariusKentState")

@app.route('/researchgate')
def researchgate():
    return redirect ("https://www.researchgate.net/profile/Marius-Paulikas")