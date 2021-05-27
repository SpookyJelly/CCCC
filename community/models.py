from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)    
    overview = models.TextField(blank=True, null=True)    
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    release_date = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    movie_id = models.CharField(max_length=100)
    red_total_score = models.IntegerField(default=0, blank=True, null=False)
    yellow_total_score = models.IntegerField(default=0, blank=True, null=False)
    purple_total_score = models.IntegerField(default=0, blank=True, null=False)
    red_count = models.IntegerField(default=0, blank=True, null=False)
    yellow_count = models.IntegerField(default=0, blank=True, null=False)
    purple_count = models.IntegerField(default=0, blank=True, null=False)
    red_average = models.FloatField(default=0, blank=True, null=False)
    yellow_average = models.FloatField(default=0, blank=True, null=False)
    purple_average = models.FloatField(default=0, blank=True, null=False)


    def __str__(self):
        return self.title


class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)   
    movie_title = models.CharField(max_length=50)
    movie_genre = models.CharField(max_length=50)
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, related_name="reviews", blank=True)
    user_rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', through='Like')
    
    def __str__(self):
        return self.title


class Like(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    add_at = models.DateTimeField(auto_now_add=True)    


class Comment(models.Model):  
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content

