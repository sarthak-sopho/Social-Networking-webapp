from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts

app = Flask(__name__)

CORS(app)

# routes: endpoints: unique endpoints used by the server to decide which data to send where
#methods like: post, get, put
#get: most common: when you make a request to see any info on internet
#post: here is some info, put it in db
#put: update
#delete: delete some info from db
#All these are CRUD, user actions
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()

    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
