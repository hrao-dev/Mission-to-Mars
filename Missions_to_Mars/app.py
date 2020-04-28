from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    mission_mars = mongo.db.mission_mars.find_one()
    return render_template("index.html", mission_mars=mission_mars)


@app.route("/scrape")
def web_scraper():
    mission_mars = mongo.db.mission_mars
    mars_data = scrape_mars.scrape()
    mission_mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
