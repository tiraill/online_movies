# Generated by Django 3.1 on 2021-01-24 18:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('rating', models.FloatField(
                    blank=True,
                    null=True,
                    validators=[django.core.validators.MinValueValidator(0)],
                    verbose_name='рейтинг'
                )),
            ],
            options={
                'verbose_name': 'кинопроизведение',
                'verbose_name_plural': 'кинопроизведения',
                'db_table': 'filmwork',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='название')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='имя')),
            ],
            options={
                'verbose_name': 'сотрудник',
                'verbose_name_plural': 'сотрудники',
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='FilmworkPersons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.TextField(
                    choices=[('actor', 'актер'), ('director', 'режиссер'), ('writer', 'сценарист')],
                    verbose_name='роль'
                )),
                ('filmwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
            options={
                'db_table': 'filmwork_persons',
                'unique_together': {('filmwork', 'person', 'role')},
            },
        ),
        migrations.CreateModel(
            name='FilmworkGenres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filmwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
            options={
                'db_table': 'filmwork_genres',
                'unique_together': {('filmwork', 'genre')},
            },
        ),
    ]
