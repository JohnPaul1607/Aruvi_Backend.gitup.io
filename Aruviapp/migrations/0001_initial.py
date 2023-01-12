# Generated by Django 4.1.3 on 2023-01-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Mobile', models.IntegerField(verbose_name=10)),
                ('Email', models.CharField(max_length=100)),
                ('Data_of_birth', models.DateField()),
                ('age', models.IntegerField(max_length=10)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('academic_year', models.CharField(max_length=10)),
                ('degree', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
            ],
        ),
    ]
