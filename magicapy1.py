from flask import Flask, request, jsonify
import random, requests, json

#below is always added to summon Flask.
app = Flask(__name__)

#the lists as below.
listweapons = ["sword", "dagger", "bow", "wand", "flail", "pole", "axe", "polearm", "glaive", "spear", "mace", "morningstar", "warhammer"]
listeffects = ["decay", "holy", "fire", "ice", "thunder", "earth", "wind", "water", "light", "shadow"]

#the main page of the API
@app.route("/")
def home():
    return "A list of weapons."

#this is where the second API will draw its weapons from, randomly as per list above, with the GET method.
@app.route("/getweapon", methods = ["GET"])
def getweapon():
    return random.choice(listweapons)

#same but for effect.
@app.route("/geteffect", methods = ["GET"])
def geteffect():
    return random.choice(listeffects)

#same for damage modifier. use randint to get your number, and make sure to add jsonify to make it legible to the other API.
#jsonify and json must be summoned at the top of the page as shown.
@app.route("/getdamage", methods = ["GET"])
def getdamage():
    return jsonify(random.randint(1, 100))
   
#the below goes in all flask pages. make sure each API is on different port, either 5000 or 5001 for localhost!
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)