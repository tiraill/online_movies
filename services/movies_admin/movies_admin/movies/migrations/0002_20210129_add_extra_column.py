# Generated by Django 3.1 on 2021-01-29 07:02

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmworkActor',
            fields=[
            ],
            options={
                'verbose_name': 'актер',
                'verbose_name_plural': 'актеры',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('movies.filmworkpersons',),
        ),
        migrations.CreateModel(
            name='FilmworkDirector',
            fields=[
            ],
            options={
                'verbose_name': 'режиссер',
                'verbose_name_plural': 'режиссеры',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('movies.filmworkpersons',),
        ),
        migrations.CreateModel(
            name='FilmworkWriter',
            fields=[
            ],
            options={
                'verbose_name': 'сценарист',
                'verbose_name_plural': 'сценаристы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('movies.filmworkpersons',),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'фильмы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('movies.filmwork',),
        ),
        migrations.CreateModel(
            name='TvShow',
            fields=[
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'сериалы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('movies.filmwork',),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='age_limit',
            field=models.CharField(blank=True, max_length=50, verbose_name='возрастной ценз'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='created',
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now, editable=False, verbose_name='created'
            ),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата создания'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата окончания'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='file_path',
            field=models.FileField(blank=True, upload_to='film_works/', verbose_name='файл'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(
                blank=True, related_name='films', through='movies.FilmworkGenres', to='movies.Genre'
            ),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now, editable=False, verbose_name='modified'
            ),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(
                blank=True, related_name='films', through='movies.FilmworkPersons', to='movies.Person'
            ),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='type',
            field=models.CharField(
                choices=[('movie', 'фильм'), ('tv_show', 'шоу')], default='movie', max_length=20, verbose_name='тип'
            ),
        ),
        migrations.RunSQL(
            "CREATE TYPE filmwork_type AS ENUM ('movie', 'tv_show'); "
            "ALTER TABLE filmwork ALTER COLUMN \"type\" TYPE filmwork_type USING type::filmwork_type;",
            "DROP TYPE filmwork_type;"
        ),
        migrations.AddField(
            model_name='genre',
            name='created',
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now, editable=False, verbose_name='created'
            ),
        ),
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='genre',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now, editable=False, verbose_name='modified'
            ),
        ),
        migrations.AddField(
            model_name='person',
            name='created',
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now, editable=False, verbose_name='created'
            ),
        ),
        migrations.AddField(
            model_name='person',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now, editable=False, verbose_name='modified'
            ),
        ),
    ]
