# Generated by Django 3.2.5 on 2023-01-31 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_studentbulkupload_csv_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbulkupload',
            name='csv_file',
            field=models.FileField(upload_to='students/bulkupload/'),
        ),
    ]
