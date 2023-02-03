# Generated by Django 4.1.5 on 2023-01-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aruviapp', '0012_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Date_of_birth',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]