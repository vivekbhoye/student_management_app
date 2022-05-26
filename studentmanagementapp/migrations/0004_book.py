# Generated by Django 4.0.4 on 2022-05-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanagementapp', '0003_alter_school_address2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('author_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Author Name')),
                ('date_of_publication', models.DateField(blank=True, null=True, verbose_name='Date of Publication')),
                ('number_of_pages', models.IntegerField(verbose_name='Number of Pages')),
            ],
        ),
    ]
