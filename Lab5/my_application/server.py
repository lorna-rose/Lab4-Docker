from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!\n"
    
@app.route("/")
def index():
    return "Index File/n"
    
@app.route("/user/paul")
def user():
    return "User Paul/n"

@app.route("/post/80")
def post():
    return "Post 80/n"

if __name__ == "__main__":
    #app.run(host="0.0.0.0")
    app.run(host='0.0.0.0',port=8080,debug=True)

