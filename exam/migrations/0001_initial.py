# Generated by Django 3.1.7 on 2021-07-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('answer1', models.CharField(max_length=200, null=True)),
                ('answer2', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
