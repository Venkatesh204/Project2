# Generated by Django 4.0.3 on 2022-04-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=30)),
                ('Occation', models.CharField(max_length=180)),
            ],
        ),
        migrations.RenameField(
            model_name='news',
            old_name='Latest_News',
            new_name='Occation',
        ),
        migrations.AlterField(
            model_name='empdata',
            name='Emp_Date_Of_Joining',
            field=models.CharField(max_length=30),
        ),
    ]
