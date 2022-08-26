from flask import Flask;

app = Flask(__name__);

@app.route("/")
def index():
    return "Sample Data from this project"

if __name__ == "__main__":
    app.run(debug = True)