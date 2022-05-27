from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story_detail', args=[str(self.id)])

class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('home')