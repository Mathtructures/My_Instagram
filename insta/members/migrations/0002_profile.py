# Generated by Django 4.2 on 2024-03-04 15:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePic', models.ImageField(upload_to='./media/img', verbose_name='pic')),
                ('title', models.CharField(max_length=60, verbose_name='Full Name')),
                ('about', models.TextField(blank=True, max_length=200, verbose_name='About...')),
                ('profID', models.CharField(max_length=50, unique=True, verbose_name='My ID')),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='followers')),
            ],
        ),
    ]
