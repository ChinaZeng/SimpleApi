# Generated by Django 3.2.9 on 2021-11-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RtmpModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=1000)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
