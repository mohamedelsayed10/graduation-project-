from google.cloud import vision
import io , os
import cv2
from googletrans import Translator

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceAccountToken.json"
client = vision.ImageAnnotatorClient()
image_path = 'test/person.jpg'
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)
response = client.object_localization(image=image)
localized_object_annotations = response.localized_object_annotations
objects = {}
objects_arabic = {}
img = cv2.imread(image_path)
width = img.shape[1]
for obj in localized_object_annotations:
    print(obj.name)

