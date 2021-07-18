# Generated by Django 3.2.4 on 2021-07-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataBaseSync', '0002_member_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='contributions',
            field=models.CharField(max_length=255, verbose_name='Сontributions in the last year'),
        ),
        migrations.AlterField(
            model_name='member',
            name='followers',
            field=models.CharField(max_length=255, verbose_name='Followers'),
        ),
        migrations.AlterField(
            model_name='member',
            name='following',
            field=models.CharField(max_length=255, verbose_name='Following'),
        ),
        migrations.AlterField(
            model_name='member',
            name='repositories',
            field=models.CharField(max_length=255, verbose_name='Repositories'),
        ),
        migrations.AlterField(
            model_name='member',
            name='stars',
            field=models.CharField(max_length=255, verbose_name='Stars'),
        ),
    ]
