import face_recognition
import numpy as np
from PIL import Image


def compare_faces(user_image, image):

    if not user_image or not image:
        return "Ikkala rasm ham kerak"

    image1 = np.array(Image.open(user_image).convert("RGB"))
    image2 = np.array(Image.open(image).convert("RGB"))

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
