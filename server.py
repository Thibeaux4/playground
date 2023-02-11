from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/<int:count>')          
def hello_world(count):
    return render_template("index.html", count=count)

if __name__=="__main__":
    app.run(debug=True)
