from rest_framework import serializers


class RecognizeSerializer(serializers.Serializer):
    image1 = serializers.ImageField()
    image2 = serializers.ImageField()

    image1_path = serializers.CharField()
    image2_path = serializers.CharField()
