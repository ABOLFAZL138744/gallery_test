from flask import Flask, request, send_file
import os

app = Flask(__name__)

os.makedirs("uploads", exist_ok=True)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file:
        return "فایلی دریافت نشد", 400

    filename = os.path.basename(file.filename)
    file.save(os.path.join("uploads", filename))

    return "فایل با موفقیت دریافت شد! 😈"

app.run(host="0.0.0.0", port=8080)
