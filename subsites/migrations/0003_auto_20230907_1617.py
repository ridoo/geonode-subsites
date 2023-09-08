# Generated by Django 3.2.20 on 2023-09-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0085_alter_resourcebase_uuid"),
        ("subsites", "0002_auto_20230907_1612"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subsite",
            name="category",
            field=models.ManyToManyField(
                blank=True, default=None, null=True, to="base.TopicCategory"
            ),
        ),
        migrations.AlterField(
            model_name="subsite",
            name="keyword",
            field=models.ManyToManyField(
                blank=True, default=None, null=True, to="base.HierarchicalKeyword"
            ),
        ),
        migrations.AlterField(
            model_name="subsite",
            name="region",
            field=models.ManyToManyField(
                blank=True, default=None, null=True, to="base.Region"
            ),
        ),
    ]
