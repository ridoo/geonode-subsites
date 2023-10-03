# Generated by Django 3.2.20 on 2023-09-11 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geonode_themes', '0014_auto_20220214_0910'),
        ('subsites', '0005_alter_subsite_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsite',
            name='resource_type',
            field=models.CharField(blank=True, choices=[('document', 'document'), ('map', 'map'), ('dataset', 'dataset'), ('dashboard', 'dashboard'), ('geoapp', 'geoapp'), ('geostory', 'geostory')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subsite',
            name='theme',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geonode_themes.geonodethemecustomization'),
        ),
    ]