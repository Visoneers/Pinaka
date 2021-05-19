# Generated by Django 3.1.1 on 2021-05-18 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_brand_color_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='store.brand'),
            preserve_default=False,
        ),
    ]