from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"
    
@app.route('/')
def index():
    return "Index Page"
    
@app.route('/user/paul')
def index():
    return "User Paul"

@app.route('/post/80')
def index():
    return "Post 80"

if __name__ == "__main__":
    #app.run(host="0.0.0.0")
    app.run(host='0.0.0.0',port=8080,debug=True)

