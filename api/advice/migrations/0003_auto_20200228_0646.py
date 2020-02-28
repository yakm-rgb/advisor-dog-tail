# Generated by Django 3.0.3 on 2020-02-28 12:46

import api.advice.models.utils
from django.db import migrations, models
from django.core.management import call_command
from django.apps import apps
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
import model_utils.fields
import uuid


def run_tag_type_fixture(apps: apps, schema_editor):
    call_command("loaddata", "tag_types")


class Migration(migrations.Migration):

    dependencies = [
        ("advice", "0002_auto_20200228_0219"),
    ]

    operations = [
        migrations.CreateModel(
            name="TagType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        populate_from="title",
                        verbose_name="slug",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
            ],
            options={"verbose_name": "Tag type", "verbose_name_plural": "Tag types",},
        ),
        migrations.RunPython(run_tag_type_fixture),
        migrations.AddField(
            model_name="tag",
            name="type",
            field=models.ForeignKey(
                default=api.advice.models.utils.get_default_tag_type,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="advice.TagType",
            ),
        ),
    ]