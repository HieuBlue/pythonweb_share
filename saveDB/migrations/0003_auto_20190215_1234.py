# Generated by Django 2.1.2 on 2019-02-15 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saveDB', '0002_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Time',
            new_name='Time_Hum_Tem',
        ),
        migrations.DeleteModel(
            name='Humidity',
        ),
        migrations.DeleteModel(
            name='Temperature',
        ),
    ]