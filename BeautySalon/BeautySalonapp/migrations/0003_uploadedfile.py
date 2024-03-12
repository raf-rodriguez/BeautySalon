# Generated by Django 5.0.3 on 2024-03-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeautySalonapp', '0002_appointment_additional_info_service_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]