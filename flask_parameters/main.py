
# importing modules 
from flask import Flask, render_template, escape
  
# declaring app name 
app = Flask(__name__) 
  
# making list of pokemons 
Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff",  
           "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"] 
  
# defining home page 
@app.route('/') 
def homepage(): 
  
# returning index.html and list 
# and length of list to html page 
    return render_template("index.html", len = len(Pokemons), Pokemons = Pokemons) 
  
# defining home page with numeric input
@app.route('/<int:post_id>') 
def homepageNum(post_id): 
  
# returning index.html and list 
# and length of list to html page 
    return render_template("index.html", len = post_id, Pokemons = Pokemons) 
  
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


if __name__ == '__main__': 
  	# running app 
    app.run(use_reloader = True, debug = True) 
