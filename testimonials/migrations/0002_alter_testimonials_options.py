# Generated by Django 4.2.10 on 2024-03-01 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonials',
            options={'ordering': ['-created_on']},
        ),
    ]
