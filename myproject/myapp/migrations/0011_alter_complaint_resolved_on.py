# Generated by Django 4.2.16 on 2024-11-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_alter_complaint_resolved_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complaint",
            name="resolved_on",
            field=models.TextField(),
        ),
    ]