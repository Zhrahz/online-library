from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.account.models import User


class Book (models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='books/')
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    score = models.IntegerField(default=0 ,validators=[MinValueValidator(1), MaxValueValidator(10)],null=True,blank=True)
    comment = models.TextField(max_length=500)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username



