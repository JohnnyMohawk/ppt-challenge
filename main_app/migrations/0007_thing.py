# Generated by Django 3.2.4 on 2021-08-24 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_place_place_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('L', 'Something I want to learn about:'), ('N', 'Something I need:'), ('W', 'Something I want:'), ('G', 'Something I am grateful for:'), ('V', 'Something I need to vent about:')], default='L', max_length=1)),
                ('name', models.CharField(max_length=50)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.challenge')),
            ],
        ),
    ]
