# Generated by Django 3.2.3 on 2021-05-26 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('poster_path', models.CharField(blank=True, max_length=200, null=True)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('release_date', models.TextField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('movie_id', models.CharField(max_length=100)),
                ('red_total_score', models.IntegerField(blank=True, default=0)),
                ('yellow_total_score', models.IntegerField(blank=True, default=0)),
                ('purple_total_score', models.IntegerField(blank=True, default=0)),
                ('red_count', models.IntegerField(blank=True, default=0)),
                ('yellow_count', models.IntegerField(blank=True, default=0)),
                ('purple_count', models.IntegerField(blank=True, default=0)),
                ('red_average', models.FloatField(blank=True, default=0)),
                ('yellow_average', models.FloatField(blank=True, default=0)),
                ('purple_average', models.FloatField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('movie_title', models.CharField(max_length=50)),
                ('movie_genre', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('user_rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hashtags', models.ManyToManyField(blank=True, related_name='reviews', to='community.Hashtag')),
                ('like_users', models.ManyToManyField(related_name='like_reviews', through='community.Like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.review'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.review')),
            ],
        ),
    ]
