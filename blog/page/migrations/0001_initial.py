# Generated by Django 4.0.5 on 2022-07-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='', max_length=200)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='page')),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('deleted', 'Silindi'), ('published', 'Yayinlandi')], default='draft', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
