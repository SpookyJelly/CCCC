from rest_framework import serializers
from accounts.serializers import AuthorSerializer, ProfileSerializer
from .models import Hashtag, Movie, Review, Comment

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'pk', 'title', 'overview', 'poster_path', 'vote_average',
            'release_date', 'genre', 'movie_id', 'red_average', 'yellow_average', 'purple_average'
        )


class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'title',
        )


class HashtagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hashtag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'pk', 'review', 'author', 'content', 
            'created_at', 'updated_at'
        )
        read_only_fields = ['review','author']


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    hashtags = HashtagSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)
    like_users = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = (
            'pk', 'author', 'title', 'movie_title',
            'content', 'hashtags', 'user_rating', 'created_at',
            'updated_at','like_users', 'comment_set',
        )
        read_only_fields = ['author', 'comment_set', 'like_users', 'hashtags']


class ReviewListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    hashtags = HashtagSerializer(many=True, read_only=True)
    like_users = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = (
            'pk', 'author', 'title', 'movie_title',
            'hashtags', 'like_users','user_rating', 'content',
        )
        read_only_fields = ['author','like_users']


