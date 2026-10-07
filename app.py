from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload():
    message = ""

    if request.method == "POST":
        file = request.files.get("file")

        if file and file.filename:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            message = "فایل با موفقیت دریافت شد."
        else:
            message = "فایلی انتخاب نشده."

    return render_template("index.html", message=message)

app.run(host="0.0.0.0", port=5000)
