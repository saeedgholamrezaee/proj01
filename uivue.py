from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="dist", static_url_path="")

# نمایش index.html
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=True)

