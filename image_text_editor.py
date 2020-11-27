from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO


class ImageTextEditor(object):
    nameFont = None
    fontTTFPath = "Cousine-Regular.ttf"
    __blankImagePath = "cbccwithoutname.png"

    BLANK_IMAGE_PATH = ""
    CO_ORDINATES_TEMP_FILE_PATH = "/tmp/card_name_coordinates.txt"
    CO_ORDINATES_S3_PATH = ""

    def __init__(self):
        self.nameFont = ImageFont.truetype(self.fontTTFPath, 22)

    @property
    def blankImagePath(self):
        # check if blank image is available here else load from S3 and then add it here
        return self.__blankImagePath

    def _getCoordinates(self):
        # look in temp path, then check in S3/EFS, then call the lambda and read from S3 again
        x, y = 48, 255
        return x, y

    def _getEditedImage(self, startX, endY, replaceWith, **kwargs):
        img = Image.open(self.blankImagePath)
        draw = ImageDraw.Draw(img)
        draw.text((startX, endY), replaceWith, font=self.nameFont, fill=(232, 232, 232))
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue())

    def getEditedImage(self, replaceWith):
        x, y = self._getCoordinates()
        return self._getEditedImage(x, y, replaceWith)


def lambda_handler(event, context):
    editor = ImageTextEditor()
    return dict(
        isBase64Encoded=True,
        statusCode=200,
        headers={'Content-Type': 'image/png'},
        body=editor.getEditedImage(event["customerName"])
    )
