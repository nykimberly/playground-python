from flask import Flask, url_for, redirect, render_template, request
from collections import Counter

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("challenge"))

def custom_challenge(text_input: str):
    arr = list(text_input.split())
    return str(sum(count // 2 for count in Counter(arr).values()))

@app.route("/challenge", methods = ["POST", "GET"])
def challenge():
    text_input = request.form.get("text_input", "")
    if request.method == "POST":
        text_output = custom_challenge(text_input)
    else:
        text_output = ""
    return render_template("challenge.html", text_input=text_input, text_output=text_output)

if __name__ == "__main__":
    app.run(debug=True)
