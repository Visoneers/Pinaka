# Generated by Django 3.1.1 on 2021-02-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210209_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='size',
            field=models.CharField(choices=[(1, 'Large'), (2, 'Small')], default=2, max_length=2),
        ),
    ]
