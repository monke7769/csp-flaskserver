from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from nlpprogram import process_text

# initialize a flask application (app)
app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')  # Allow all origins (*)

# ... your existing Flask
# add an HTML endpoint to flask app
@app.route('/')
def say_hello():
    html_content = """
    <html>
    <head>
        <title>Text to Python</title>
    </head>
    <body>
        <h1>Enter Text</h1>
        <form id="textForm">
            <input type="text" id="textInput" placeholder="Enter text">
            <button type="submit">Submit</button>
        </form>
        <div id="response"></div>

       <script>
            document.getElementById("textForm").addEventListener("submit", function (e) {
               e.preventDefault();
               const textInput = document.getElementById("textInput").value;

               fetch("/submit", {
                method: "POST",
                    headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ text: textInput }),
            })
                .then((response) => response.json())
                .then((data) => {
                    document.getElementById("response").innerText = data.message;
                });
        });
    </script>
    </html>
    """
    return html_content
@app.route('/submit', methods=['POST'])
def submit():
    text = request.json.get('text')
    result = process_text(text)  # Call the function from nlpprogram.py
    return jsonify({'message': result})

if __name__ == '__main__':
    # starts flask server on default port, http://127.0.0.1:5001
    app.run(port=5001)