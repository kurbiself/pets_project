# Generated by Django 4.2 on 2024-10-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_list', '0004_alter_petstypes_options_alter_petstypes_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='breeds',
            options={'verbose_name': 'Тип породы', 'verbose_name_plural': 'Типы пород'},
        ),
        migrations.AlterModelOptions(
            name='pets',
            options={'verbose_name': 'Питомцы', 'verbose_name_plural': 'Питомец'},
        ),
        migrations.AlterModelOptions(
            name='petsowners',
            options={'verbose_name': 'Владельцы', 'verbose_name_plural': 'Владелец'},
        ),
        migrations.AlterField(
            model_name='breeds',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='breeds',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Заметки'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Заметки'),
        ),
        migrations.AlterField(
            model_name='petsowners',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Имя'),
        ),
    ]