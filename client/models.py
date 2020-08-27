from django.db import models

from django_resized import ResizedImageField

def client_image_upload_to(instance, filename):
    """
    Upload the client image into the path and return the uploaded image path.
    """
    path = f"clients/{instance.name}/{filename}"
    return path

class Client(models.Model):
    """
    Client model.
    """
    name       = models.CharField(max_length=255)
    image      = ResizedImageField(size=[241, 173], quality=100, upload_to=client_image_upload_to)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        # return the client name
        return self.name

        