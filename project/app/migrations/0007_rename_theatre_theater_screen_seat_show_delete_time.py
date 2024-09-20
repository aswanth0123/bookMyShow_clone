# Generated by Django 5.0.8 on 2024-09-17 04:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_theatre_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Theatre',
            new_name='Theater',
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_number', models.IntegerField()),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screens', to='app.theater')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10)),
                ('seat_type', models.CharField(choices=[('Regular', 'Regular'), ('Premium', 'Premium')], max_length=20)),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='app.screen')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='app.movie')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='app.screen')),
            ],
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]
