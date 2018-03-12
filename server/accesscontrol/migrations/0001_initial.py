# Generated by Django 2.0.1 on 2018-02-01 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='event occurred')),
                ('event_type', models.CharField(choices=[('0', 'authorized'), ('1', 'tag not found'), ('2', 'invalid password'), ('3', 'insufficient privileges')], max_length=50)),
                ('reader_position', models.CharField(choices=[('0', 'outside'), ('1', 'inside')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rfid_tag', models.CharField(max_length=8)),
                ('hashed_password', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accesscontrol.Room'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accesscontrol.User'),
        ),
    ]