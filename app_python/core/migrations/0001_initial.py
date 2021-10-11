# Generated by Django 3.2.6 on 2021-10-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visits', models.IntegerField(default=0)),
                ('user_agent', models.TextField(null=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
        ),
    ]
