from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    text = request.json.get("text")
    
    # Pass the input text to nlpprogram.py using subprocess
    command = ["python", "nlpprogram.py", text]
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        response = {"message": result.strip()}
    except subprocess.CalledProcessError as e:
        response = {"error": str(e)}
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
