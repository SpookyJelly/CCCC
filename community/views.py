from django.http.response import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer, ReviewSerializer, ReviewListSerializer, CommentSerializer, MovieTitleSerializer
from .models import Movie, Review, Comment, Hashtag


# Create your views here.
@api_view(['GET'])
def index(request):   
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)     


@api_view(['GET'])
def movie_title(request):
    movies = Movie.objects.all()
    serializer = MovieTitleSerializer(movies, many=True)
    return Response(data=serializer.data)        


@api_view(['GET','POST'])
def review_list(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            reviews = Review.objects.all()
            serializer = ReviewListSerializer(reviews, many=True)
            return Response(data=serializer.data)
        elif request.method == "POST":        
            serializer = ReviewSerializer(data=request.data)                                    
            if serializer.is_valid(raise_exception=True):
                review = serializer.save(author=request.user)         
                #해시태그                
                # print(serializer.data) # 유효성 검증 후 데이터
                # print(serializer.initial_data) # 유효성 검증 전 데이터
                hashtags = serializer.initial_data.get('hashtags')
                if hashtags:
                    for tag in hashtags.split():
                        hashtag, created = Hashtag.objects.get_or_create(content=tag)
                        review.hashtags.add(hashtag)
                        # print(review.hashtags.all())
                # 평점 카운트 부분
                movie = Movie.objects.filter(title=serializer.data['movie_title'])[0]                              
                if request.user.groupcolor == 'red':               
                    movie.red_total_score += int(serializer.data['user_rating'])
                    movie.red_count += int(1) 
                    movie.red_average = int(movie.red_total_score) / int(movie.red_count)    
                    movie.save()      
                elif request.user.groupcolor == 'yellow':               
                    print(serializer.data['user_rating'])
                    print(type(serializer.data['user_rating']))
                    movie.yellow_total_score += int(serializer.data['user_rating'])
                    movie.yellow_count += int(1) 
                    movie.yellow_average = int(movie.yellow_total_score) / int(movie.yellow_count)    
                    movie.save()   
                else:              
                    movie.purple_total_score += int(serializer.data['user_rating'])
                    movie.purple_count += int(1)
                    movie.purple_average = int(movie.purple_total_score) / int(movie.purple_count)    
                    movie.save()   
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return HttpResponse(status=401)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_id):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, id=review_id)
        if request.method == "GET":        
            serializer = ReviewSerializer(review)
            return Response(data=serializer.data)
        elif request.method == "PUT":
            if request.user == review.author:
                serializer = ReviewSerializer(review, data=request.data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data=serializer.data)
            return HttpResponse(status=401)
        elif request.method == "DELETE":
            if request.user == review.author:
                data = {
                    'message' : "리뷰가 삭제되었습니다."
                }
                review.delete()
                return Response(data=data,status=status.HTTP_204_NO_CONTENT)
            return HttpResponse(status=401)
    return HttpResponse(status=401)
        

@api_view(['GET', 'POST'])
def comment_list(request, review_id):
    if request.user.is_authenticated: 
        review = get_object_or_404(Review, id=review_id)  
        if request.method == "GET":  
            comments = review.comment_set.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(data=serializer.data)
        elif request.method == "POST":          
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(review=review, author=request.user)
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return HttpResponse(status=401)


@api_view(['PUT', 'DELETE'])
def comment_detail(request, review_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "PUT":
        if request.user == comment.author:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        return HttpResponse(status=401)
    elif request.method == "DELETE":
        if request.user == comment.author:
            data = {
                'message' : "댓글이 삭제되었습니다."
            }
            comment.delete()
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)
        return HttpResponse(status=401)


@api_view(['POST'])
def review_like(request, review_id):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_id)
        if review.like_users.filter(pk=request.user.id).exists():
            review.like_users.remove(request.user)
            liked = False
        else:
            review.like_users.add(request.user)
            liked = True
        data = {
            'liked': liked,
            'user_count': review.like_users.count(),
        }
        return JsonResponse(data=data, status=status.HTTP_200_OK)
    return HttpResponse(status=401)


@api_view(['GET'])
def review_search(request):  
    keyword = request.GET.get('q')
    def hashtag(tags):
        tag_list = tags.split() 
        reviews = Review.objects.filter(hashtags__content__in=tag_list).distinct()     
        serializer = ReviewSerializer(reviews, many=True)
        return serializer
    serializer = hashtag(keyword)    

    return Response(data=serializer.data, status=status.HTTP_200_OK)




