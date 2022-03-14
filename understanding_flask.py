from flask import Flask
app = Flask(__name__)











@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_hi():
    if ('/say/<name>') =! 
    return f'Hi,{name}!'

@app.route("/math/<int:num>/<name>")
def do_math(num):
    newArr = []
    for i in range(0,num+1, 1):
        newArr.append(i)
        return f"{str:name}"

















if __name__=="__main__":
    app.run(debug=True)

