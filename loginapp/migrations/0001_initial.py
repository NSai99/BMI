# Generated by Django 3.0 on 2020-10-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Migration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.BooleanField(default=0)),
                ('weight', models.IntegerField()),
                ('Height', models.FloatField()),
                ('BMI', models.FloatField()),
                ('Index', models.CharField(max_length=100)),
            ],
        ),
    ]
