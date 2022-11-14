from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import mark_safe
from users.models import User

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Appliance(models.Model):

    name = models.CharField(max_length=100, blank=False)
    serial_number = models.CharField(max_length=20, blank=True, default='')
    creation_time = models.DateTimeField()
    description = models.TextField()
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name + " SN:" + self.serial_number)


class AppliancePhoto(models.Model):
    image = models.ImageField(upload_to='images/')
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    image_added_time = models.DateTimeField(auto_now_add=True)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""
        
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True 