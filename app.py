from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")

def HomePage(name=None):
    
    return render_template('index.html',name=name)

# @app.route("/chat")
# def ChatAnswer():
    
if __name__ == "__main__":

    app.run(debug=True)