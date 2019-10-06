
# importing modules 
from flask import Flask, render_template, redirect
  
# declaring app name 
app = Flask(__name__) 

@app.route('/')
def index():
	return redirect("/main", code=302)
  
@app.route('/main') 
def main():
	return render_template("main.html")

@app.route('/about') 
def about():
	return render_template("about.html")

@app.route('/settings') 
def settings():
	return render_template("settings.html")
	

if __name__ == '__main__': 
  	# running app 
    app.run(use_reloader = True, debug = True) 
