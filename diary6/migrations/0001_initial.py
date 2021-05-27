# Generated by Django 3.2.2 on 2021-05-27 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('body', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='diary6/')),
            ],
        ),
    ]
