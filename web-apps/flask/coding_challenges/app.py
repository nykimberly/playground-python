from flask import Flask, url_for, redirect, render_template, request
from collections import Counter

app = Flask(__name__)

def sockMerchant(sock_types):
    return str(sum(count // 2 for count in Counter(sock_types.split()).values()))

def countingValleys(path):
    num_valleys = 0
    altitude = 0
    for step in path:
        altitude += 1 if step == "U" else -1
        if altitude == 0 and step == "U":
            num_valleys += 1
    return num_valleys

CHALLENGES = {
    "sockmerchant": sockMerchant,
    "countingvalleys": countingValleys
}

@app.route("/")
def index():
    return redirect(url_for("challenge"))

@app.route("/challenge")
def challenge():
    return render_template(
        "challenge.html", challenges=CHALLENGES.keys())

@app.route("/challenge/<challenge_name>", methods = ["POST", "GET"])
def challenge_form(challenge_name):
    text_input = request.form.get("text_input", "")
    challenge = CHALLENGES.get(challenge_name, "")
    if request.method == "POST" and challenge:
        text_output = challenge(text_input)
    else:
        text_output = ""
    return render_template(
        "challenge_form.html",
        challenge_name=challenge_name, text_input=text_input, text_output=text_output)

if __name__ == "__main__":
    app.run(debug=True)
