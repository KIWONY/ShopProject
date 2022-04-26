from rest_framework import serializers

from accountapp.models import Comment


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length= 50)
    comment = serializers.CharField(max_length=500)
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.email =validated_data.get("email",instance.email)
        instance.password = validated_data.get("password", instance.password)
        instance.comment = validated_data.get("comment", instance.comment)
        instance.created_at = validated_data.get("created_at", instance.created_at)

        instance.save()
        return instance