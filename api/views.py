from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.views import APIView, Response
from rest_framework import generics
from rest_framework.decorators import api_view


from project.utils import compare_faces, get_image_from_url
from .serializers import RecognizeSerializer


class RecognizeAPIView(generics.CreateAPIView):
    serializer_class = RecognizeSerializer

    def post(self, request, *args, **kwargs):

        faceOne = request.FILES.get("faceOne")
        faceTwo = request.FILES.get("faceTwo")

        image1_path = request.POST.get("image1_path")
        image2_path = request.POST.get("image2_path")

        try:
            if faceOne and faceTwo:
                result = compare_faces(faceOne, faceTwo)

            elif image1_path and image2_path:
                result = compare_faces(image1=get_image_from_url(image1_path), image2=get_image_from_url(image2_path))

            elif faceOne and image1_path:
                result = compare_faces(faceOne, get_image_from_url(image1_path))

            else:
                return Response({"message": "Rasm to'g'ri yuklanmagan"}, status=400)

            return Response({"message": result[0]}, status=result[1])

        except Exception as e:
            return Response({"message": str(e)}, status=400)
