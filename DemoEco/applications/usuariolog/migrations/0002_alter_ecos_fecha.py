# Generated by Django 4.0.5 on 2022-07-04 08:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuariolog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 10, 17, 10, 622259), editable=False),
        ),
    ]
