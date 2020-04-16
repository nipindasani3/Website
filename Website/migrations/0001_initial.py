# Generated by Django 2.2.12 on 2020-04-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Olympics',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('sport', models.CharField(max_length=20)),
                ('discipline', models.CharField(max_length=30)),
                ('athlete', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=5)),
                ('event', models.CharField(max_length=50)),
                ('medal', models.CharField(max_length=10)),
            ],
        ),
    ]
