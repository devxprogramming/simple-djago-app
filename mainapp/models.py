from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch.dispatcher import receiver
from PIL import Image
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20)
    qr_code = models.ImageField(upload_to='qr_codes/', unique=True, editable=False)

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"{self.name} ({self.roll_number})")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        self.qr_code.save(f"{self.name}.png", ContentFile(buffer.getvalue()), save=False)
        buffer.close()
        img.close()
        
    def save(self, *args, **kwargs):
        self.generate_qr_code()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}"

