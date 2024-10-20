# Generated by Django 5.1.1 on 2024-10-20 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_student_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='qr_code',
            field=models.ImageField(default=True, editable=False, unique=True, upload_to='qr_codes/'),
            preserve_default=False,
        ),
    ]
