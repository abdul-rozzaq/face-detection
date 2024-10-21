from io import BytesIO

import face_recognition
import numpy as np
import requests

from PIL import Image


def get_image_from_url(url):
    response = requests.get(url)
    return BytesIO(response.content)


def compare_faces(image1, image2):

    if not image1 or not image2:
        return "Ikkala rasm ham kerak"

    image1 = np.array(Image.open(image1).convert("RGB"))
    image2 = np.array(Image.open(image2).convert("RGB"))

    try:
        image1_encoding = face_recognition.face_encodings(image1)
        image2_encoding = face_recognition.face_encodings(image2)

    except RuntimeError:
        return "Aniqlashni iloji bo'lmadi, Qayta urinib ko'ring"

    if len(image1_encoding) == 0 or len(image2_encoding) == 0:
        return "Yuzlardan biri yoki ikkalasi topilmadi"

    natija = face_recognition.compare_faces([image1_encoding[0]], image2_encoding[0])

    print("Natijalar:", natija)

    if natija[0]:
        return "Yuzlar mos keldi"
    else:
        return "Yuzlar mos kelmadi"
