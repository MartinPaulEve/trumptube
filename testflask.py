from flask import Flask
from flask import render_template

# set static folder
app = Flask(__name__, static_url_path='/static')

@app.route("/")
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="Alex"):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run()