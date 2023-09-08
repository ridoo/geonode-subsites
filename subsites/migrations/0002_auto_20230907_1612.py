# Generated by Django 3.2.20 on 2023-09-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0085_alter_resourcebase_uuid"),
        ("subsites", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subsite",
            name="category",
            field=models.ManyToManyField(null=True, to="base.TopicCategory"),
        ),
        migrations.AddField(
            model_name="subsite",
            name="keyword",
            field=models.ManyToManyField(null=True, to="base.HierarchicalKeyword"),
        ),
        migrations.AddField(
            model_name="subsite",
            name="region",
            field=models.ManyToManyField(null=True, to="base.Region"),
        ),
        migrations.AlterField(
            model_name="subsite",
            name="slug",
            field=models.SlugField(
                help_text="Sub site name, formatted as slug",
                max_length=250,
                verbose_name="Site name",
            ),
        ),
    ]