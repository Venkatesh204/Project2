# Generated by Django 4.0.3 on 2022-04-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_empdata_emp_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdata',
            name='Emp_Date_Of_Joining',
            field=models.IntegerField(),
        ),
    ]
