# Generated by Django 3.0 on 2020-01-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('other_names', models.CharField(max_length=30)),
                ('identification_number', models.IntegerField()),
                ('nssf_number', models.IntegerField()),
                ('nhif_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('employee_number', models.IntegerField()),
                ('employee_position', models.CharField(max_length=30)),
            ],
        ),
    ]