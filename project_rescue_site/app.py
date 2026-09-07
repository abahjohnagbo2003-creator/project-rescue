from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Demo project data. Replace these values with your real ministry information
# before publishing the site.
MINISTRY = {
    "name": "Project Rescue",
    "tagline": "A place for a new purpose.",
    "city": "Decatur, Alabama",
    "address": "179 Cave Spring Road, Decatur, AL 35603",
    "phone": "+1 (256) 274-3468",
    "email": "ronniecrocker1@gmail.com",
}

@app.route("/")
def home():
    return render_template("index.html", ministry=MINISTRY)

@app.route("/prayer", methods=["POST"])
def prayer():
    # Demo-only form: this does not store sensitive prayer requests.
    name = request.form.get("name", "").strip()
    return redirect(url_for("home") + "#thank-you")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
