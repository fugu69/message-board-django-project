from django.db import models

class Post(models.Model):
    post_content = models.TextField()

    def __str__(self) -> str:
        return self.post_content[:50]