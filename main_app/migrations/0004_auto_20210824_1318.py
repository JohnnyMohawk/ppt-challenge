# Generated by Django 3.2.4 on 2021-08-24 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_selected_type_people_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='type',
            field=models.CharField(choices=[('L', 'Person to learn about:'), ('C', 'Person to reach out to:'), ('G', 'Person I am grateful for:')], default='L', max_length=1),
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('L', 'Place to learn about:'), ('T', 'Place to travel to:'), ('G', 'Place I am grateful for:')], default='L', max_length=1)),
                ('place', models.CharField(max_length=50)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.challenge')),
            ],
        ),
    ]