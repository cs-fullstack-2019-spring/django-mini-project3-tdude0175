# Generated by Django 2.0.6 on 2019-03-01 16:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teacherRecordApp', '0003_auto_20190301_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classrecordmodel',
            name='entryDate',
            field=models.DateField(default=datetime.datetime(2019, 3, 1, 16, 50, 46, 656962, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='classrecordmodel',
            name='workDate',
            field=models.DateField(default=datetime.datetime(2019, 3, 1, 16, 50, 46, 656939, tzinfo=utc)),
        ),
    ]
