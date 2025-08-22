from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    #W check which tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #Generic way to identity an object, we first need the Type of the object in a form of a (product, video, etc) and the second is the ID of that object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() # With this 2 pieces of information, then we can identify any object in our application
    content_object = GenericForeignKey()

