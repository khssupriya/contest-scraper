from .services import ImageGenerator
from flask import(Blueprint)
import io
from flask import send_file


bluePrint = Blueprint('router', __name__)


@bluePrint.route('/')
def index():
    response = {"data": "Index Route"}
    return response


@bluePrint.route('/download')
def test():
    imageGenerator = ImageGenerator()
    generatedImages = imageGenerator.generateImages()
    imageIO = io.BytesIO()
    generatedImages[0].save(imageIO, 'JPEG', quality=100)
    imageIO.seek(0)
    return send_file(imageIO, mimetype='image/jpeg')
