# Generated by Django 3.2.8 on 2021-10-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_add_related_name_to_house_FK_of_zillow_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zillowlisting',
            name='id',
            field=models.BigIntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]
