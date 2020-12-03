from flask import Flask, render_template, url_for
from app import app


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/signin')
def signin():
	return render_template('signin.html')