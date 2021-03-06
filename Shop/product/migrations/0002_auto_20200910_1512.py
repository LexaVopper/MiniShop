# Generated by Django 3.1.1 on 2020-09-10 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/media/products_images/')),
                ('is_active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
