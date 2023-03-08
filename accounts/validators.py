from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1] # cover-image.jpg jpg is [1]
    print(ext)
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if ext.lower() not in valid_extensions:
        raise ValidationError(
            f'Unsupported file extension. Allowed extensions:{valid_extensions}'
        )