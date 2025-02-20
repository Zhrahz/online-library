from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.book.models import Book, Comment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        model = Comment
        fields = "__all__"

    def validate(self, attrs):
        score=attrs.get("score", None)
        if score and not  self.context["request"].user.is_authenticated:
                raise ValidationError("برای ثبت امتیاز به همراه نظر باید به سامانه وارد شوید")

        is_confirmed = attrs.get("is_confirmed", None)
        if is_confirmed and self.context['request'].user.role != "admin":
            raise ValidationError("شما قادر به این کار نیستید")
        return super().validate(attrs)


