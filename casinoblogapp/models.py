from django.db import models
from datetime import datetime
from storages.backends.s3boto3 import S3Boto3Storage

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateField(default=datetime.utcnow())

    def __str__(self):
        return self.title
    
class Image(models.Model):
    image = models.ImageField(storage=S3Boto3Storage(), default="www.google.com")
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_id.title