# Generated by Django 4.1.3 on 2022-11-19 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imoji', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('content', models.TextField(max_length=200)),
                ('privacy', models.CharField(choices=[('나만보기', '나만보기'), ('일부공개', '일부공개'), ('전체공개', '전체공개')], max_length=10)),
                ('color', models.CharField(blank=True, max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('temperature', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
