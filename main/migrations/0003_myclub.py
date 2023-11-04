# Generated by Django 4.2.7 on 2023-11-04 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_club_meet_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.club')),
            ],
        ),
    ]