# Generated by Django 3.0.6 on 2020-11-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('http_stubs', '0003_translation_model_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='path',
            field=models.URLField(max_length=2000, verbose_name='Full request path'),
        ),
    ]