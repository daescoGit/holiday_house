# Generated by Django 3.0.6 on 2020-05-29 12:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.UUID('35495c77-0fed-49d4-be17-96cdb46a699a'), unique=True)),
                ('order', models.IntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Property')),
            ],
        ),
    ]
