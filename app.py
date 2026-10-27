
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Student Information</title>
        </head>
        <body>
            <h1>Student Information</h1>
            <p>Name: Arun Kumar</p>
            <p>Registration Number: 24MIS1001</p>
            <p>Department: Software Engineering</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
