# HTTP SCREEN MIRRORING

# Code by Rakarmp on Github

# This code is a part of the project "HTTP SCREEN MIRRORING"
# Require Python 3.6 or higher
# Require Flask, Pillow

from io import BytesIO
from flask import Flask, send_file, request
from PIL import ImageGrab

app = Flask(__name__)

@app.route("/")
def home_page():
    res = send_file("index.html", mimetype="text/html")
    return res

@app.route("/screenshot")
def img_screenshot():
    img_byte_arr = BytesIO()
    img_quality = request.args.get("quality", default=70, type=int)
    img_size = request.args.get("size", default=100, type=int)

    scale_factor = img_size / 100

    img = ImageGrab.grab()
    img_w = int(img.size[0] * scale_factor)
    img_h = int(img.size[1] * scale_factor)
    img.resize((img_w, img_h)).save(img_byte_arr, format="JPEG", quality=img_quality)
    img_byte_arr.seek(0)

    res = send_file(img_byte_arr, mimetype="image/jpeg")

    return res

if __name__ == '__main__':
    svhost = "0.0.0.0"
    svport = 8099
    app.run(svhost, svport)
