# Generated by Django 4.0.3 on 2022-04-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_empdata_emp_date_of_joining'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latest_News', models.CharField(max_length=180)),
            ],
        ),
    ]
