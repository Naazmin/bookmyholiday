# Generated by Django 3.2 on 2021-06-10 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_mybookings_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquery',
            name='reply',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='enquery',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
