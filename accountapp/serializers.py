from rest_framework import serializers

from accountapp.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        comments = serializers.StringRelatedField(many=True)
        model = Comment

        fields = ("email","password","comment","create_at")
