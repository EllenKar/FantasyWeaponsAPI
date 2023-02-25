from flask import Flask, request, jsonify
import requests, json, random

app = Flask(__name__)

randstat = ["Amazing!", "Use it well!", "Very useful!", "This'll come in handy!", "Looks so powerful!"]

@app.route("/")
def home():
    return "You open the magic chest! Which weapon do you get?"

#summon your data from other API with the below! set up a new route for it and use requests and the command you used in the other API
#we used GET to get the other data so we use GET here, make sure to add JSON for the number of the damage modifier. the others are text.
#there's also a neat way to add a random element in an f string directly, as below. simply create the list for the random result above.
@app.route("/gettheweapon")
def gettheweapon():
    res1 = requests.get("http://localhost:5000/getweapon").text
    res2 = requests.get("http://localhost:5000/geteffect").text
    res3 = requests.get("http://localhost:5000/getdamage").json()
    return f"You get a {res1} of {res2} with a damage modifier of {res3}! {random.choice(randstat)}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
