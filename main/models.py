from djongo import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os
from datetime import datetime
# Create your models here.
class MediaDrivea(models.Model):
    author = models.ForeignKey(
        User, related_name='author', on_delete=models.DO_NOTHING, null=True)
    image = models.FileField(upload_to='uploads', max_length=500)
    video = models.FileField(upload_to='uploads',max_length=250,null=True,blank=True)
    created_document_timestamp = models.DateTimeField(
        default=datetime.now())

    def __str__(self):
        return str(self.image.name)
    


    
class VideoModel(models.Model):
    video = models.FileField(
        upload_to='uploads', max_length=250, null=True, blank=True)
    

    def __str__(self):
        return str(self.video.name)
