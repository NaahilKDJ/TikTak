# Generated by Django 5.1 on 2024-11-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=150)),
                ('nom', models.CharField(max_length=150)),
                ('prenom', models.CharField(max_length=150)),
                ('dateDeNaissance', models.DateField()),
                ('dateCreationCompte', models.DateField()),
                ('private', models.BooleanField(default=True)),
                ('profilePic', models.FileField(upload_to='')),
            ],
        ),
    ]
