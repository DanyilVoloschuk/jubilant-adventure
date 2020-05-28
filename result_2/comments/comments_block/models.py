from django.db import models


class Comment(models.Model):
    user_name = models.CharField(max_length=200)
    comment_text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.user_name
