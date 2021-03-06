# Generated by Django 3.2.4 on 2021-07-15 18:41

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_add_new_movies_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created'
                )),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified'
                )),
                ('name', models.CharField(max_length=512, unique=True, verbose_name='канал')),
                ('code', models.CharField(max_length=512, unique=True, verbose_name='код')),
            ],
            options={
                'verbose_name': 'канал нотификации',
                'verbose_name_plural': 'каналы нотификаций',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created'
                )),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified'
                )),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('user_id', models.UUIDField(unique=True, verbose_name='uuid пользователя')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created'
                )),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified'
                )),
                ('name', models.CharField(max_length=512, unique=True, verbose_name='нотификация')),
                ('code', models.CharField(max_length=512, unique=True, verbose_name='код')),
            ],
            options={
                'verbose_name': 'нотификации',
                'verbose_name_plural': 'нотификация',
            },
        ),
        migrations.CreateModel(
            name='AllowChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created'
                )),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified'
                )),
                ('enabled', models.BooleanField(default=True, verbose_name='Включен')),
                ('channel', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='notification.channel', verbose_name='канал'
                )),
                ('client', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='notification.client', verbose_name='пользователь'
                )),
                ('notify', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='notification.notify', verbose_name='нотификация'
                )),
            ],
            options={
                'verbose_name': 'канал пользователя',
                'verbose_name_plural': 'каналы пользователя',
                'unique_together': {('channel', 'notify', 'client')},
            },
        ),
    ]
