from django.db import models
from django.db.models.signals import pre_save
from Content.thum import thum


class Content(models.Model):
    name = models.CharField(max_length=120)
    FILE_CHOICES = (
        ('img', 'Image'),
        ('vid', 'Video'),
        ('aud', 'Audio'),
        ('txt', 'Text'),
        )
    type = models.CharField(max_length=120, choices=FILE_CHOICES)
    file = models.FileField(upload_to='content/')
    thumbnail = models.ImageField(blank=True, null=True)
    test = models.CharField(max_length=123,null=True,blank=True)
    def __str__(self):
        return self.name

def thumbnail_pre_save_receiver(sender,instance,*args,**kwargs):
        #instance.test = '2'
        #print(instance.type)
        if instance.type == 'img':
            # instance.test = '1'
            # print("........................")
            # print(instance.file)
            # print(instance.file)
            instance.thumbnail = '/thumbnail/Thummbnailimage.png'
        if instance.type == 'vid':
            instance.thumbnail = '/thumbnail/Thumbnailvideo.png'
        if instance.type == 'aud':
            instance.thumbnail = '/thumbnail/Thumbnailaudio.png'
        if instance.type == 'txt':
            instance.thumbnail = '/thumbnail/Thumbnailtext.png'
pre_save.connect(thumbnail_pre_save_receiver,sender=Content)
