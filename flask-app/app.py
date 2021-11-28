from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# list of cat images
images = [
    "/static/gifs/0.gif",
    "/static/gifs/1.gif",
    "/static/gifs/2.gif",
    "/static/gifs/3.gif",
    "/static/gifs/4.gif",
    "/static/gifs/5.gif",
    "/static/gifs/7.gif",
    "/static/gifs/8.gif",
    "/static/gifs/9.gif",
    "/static/gifs/10.gif",
    "/static/gifs/11.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    # Uncomment to run on Heroku. 
    app.run(host="0.0.0.0", port=os.environ['PORT'])

    # Uncomment to run locally.
    #app.run(host="0.0.0.0")
