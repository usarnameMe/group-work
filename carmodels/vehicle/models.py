import os

from PIL import Image
from django.core.exceptions import ValidationError
from django.db import models


def validate_image(image):
    file_size = image.size

    allowed_formats = ['JPEG', 'PNG', 'GIF', 'BMP', 'TIFF']

    if file_size > 2 * 1024 * 1024:
        raise ValidationError("Max file size is 2MB")

    try:
        img = Image.open(image)
        if img.format not in allowed_formats:
            raise ValidationError(f"Unsupported file format. Allowed formats: {', '.join(allowed_formats)}")
    except Exception as e:
        raise ValidationError("Invalid image file.")


class Vehicle(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField(blank=True)
    picture = models.ImageField(upload_to='vehicle_pictures/', blank=True, null=True, validators=[validate_image])

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
