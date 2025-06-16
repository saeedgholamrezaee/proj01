from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="build", static_url_path="")

# نمایش index.html
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# نمایش فایل‌های استاتیک مثل js, css, images
#@app.route("/<path:path>")
#def static_files(path):
#    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True)

