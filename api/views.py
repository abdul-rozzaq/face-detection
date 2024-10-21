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

        image1 = request.FILES.get("image1")
        image2 = request.FILES.get("image2")

        image1_path = request.POST.get("image1_path")
        image2_path = request.POST.get("image2_path")

        if image1 and image2:
            result = compare_faces(image1, image2)

        elif image1_path and image2_path:
            result = compare_faces(image1=get_image_from_url(image1_path), image2=get_image_from_url(image2_path))

        elif image1 and image1_path:
            result = compare_faces(image1, get_image_from_url(image1_path))

        else:
            return Response({"message": "Rasm to'g'ri yuklanmagan"})

        return Response({"message": result})


# class RecognizeUrlsAPIView(generics.CreateAPIView):
#     serializer_class = RecognizeUrlsSerializer

#     def post(self, request, *args, **kwargs):

#         image1_path = request.POST.get("image1_path")
#         image2_path = request.POST.get("image2_path")

#         if image1_path and image2_path:

#             result = compare_faces(
#                 get_image_from_url(image1_path),
#                 get_image_from_url(image2_path),
#             )

#             return Response({"message": result})

#         return Response({"message": "Rasm to'g'ri yuklanmagan"})
