# Generated by Django 3.1 on 2021-07-21 15:05

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StripePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created'
                )),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified'
                )),
                ('stripe_id', models.CharField(max_length=250, verbose_name='id в stripe')),
                ('billing_id', models.CharField(max_length=250, verbose_name='id в billing')),
            ],
            options={
                'verbose_name': 'цены',
                'verbose_name_plural': 'цена',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='StripeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created'
                )),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified'
                )),
                ('stripe_id', models.CharField(max_length=250, verbose_name='id в stripe')),
                ('billing_id', models.CharField(max_length=250, verbose_name='id в billing')),
            ],
            options={
                'verbose_name': 'продукты',
                'verbose_name_plural': 'продукт',
                'ordering': ['-id'],
            },
        ),
    ]
