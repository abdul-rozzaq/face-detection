from rest_framework import serializers


class RecognizeSerializer(serializers.Serializer):
    faceOne = serializers.ImageField()
    faceTwo = serializers.ImageField()

    # image1_path = serializers.CharField()
    # image2_path = serializers.CharField()
