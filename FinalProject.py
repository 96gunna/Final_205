from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from PIL import Image
from io import BytesIO
import random
import base64

app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = 'lilboi'


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def user_upload():
    file = request.files['file']
    image_data = file.read();
    image = Image.open(BytesIO(image_data))
    image_data_base64 = base64.b64encode(image_data).decode('utf-8')
    # image.show()  # Test to show that we get the image
    return render_template('upload.html', image_data_base64=image_data_base64)


@app.route('/examples', methods=('GET', 'POST'))
def show_examples():
    return render_template('examples.html')