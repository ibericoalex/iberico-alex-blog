# Generated by Django 4.2.10 on 2024-02-25 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0003_testimonial_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['-created_on']},
        ),
    ]