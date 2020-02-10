# Generated by Django 2.2 on 2020-02-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination_app', '0001_initial'),
        ('user_app', '0006_auto_20200201_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='guideregistermodel',
            old_name='contact',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='guideregistermodel',
            old_name='password1',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='touristregistermodel',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='guideregistermodel',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='touristregistermodel',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='guideregistermodel',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='guideregistermodel',
            name='locations',
        ),
        migrations.AddField(
            model_name='guideregistermodel',
            name='locations',
            field=models.ManyToManyField(to='destination_app.DestinationModel'),
        ),
        migrations.AddField(
            model_name='guideregistermodel',
            name='languages',
            field=models.ManyToManyField(to='user_app.LanguageModel'),
        ),
    ]
