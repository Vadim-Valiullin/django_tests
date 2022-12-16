# Generated by Django 4.1.3 on 2022-11-10 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('lat', models.CharField(max_length=80, verbose_name='Ширина')),
                ('lng', models.CharField(max_length=80, verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=100, verbose_name='Логин')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('role', models.CharField(max_length=100, verbose_name='Роль')),
                ('age', models.SmallIntegerField(verbose_name='Возраст')),
                ('location', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ads.location')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('image', models.ImageField(default='No images', upload_to='images/')),
                ('author', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ads.user')),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ads.category')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]