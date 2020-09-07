# Generated by Django 3.0.6 on 2020-05-25 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=200)),
                ('avalible', models.BooleanField(default=True)),
                ('picture', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Boocking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Album')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Contact')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='albums', to='store.Artist'),
        ),
    ]
