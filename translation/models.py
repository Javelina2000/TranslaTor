import uuid
from django.db import models

# Create your models here.

class TranslationCard(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    translate_request = models.TextField(max_length=2000, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='uploaded')

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.name