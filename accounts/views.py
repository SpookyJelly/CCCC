from community.serializers import ReviewSerializer
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileUpdateSerializer, ProfileSerializer
from django.contrib.auth import get_user_model



# Create your views here.
@api_view(['GET'])
def user_profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)          
    serializer = ProfileSerializer(person)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def profile(request):
    person = get_object_or_404(get_user_model(), username=request.user.username)     
    serializer = ProfileSerializer(person)
    return Response(data=serializer.data, status=status.HTTP_200_OK)   
   

@api_view(['GET', 'PUT'])
def profile_update(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    if request.user == person:
        if request.method == "GET":
            serializer = ProfileUpdateSerializer(person)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        elif request.method == "PUT":
            serializer = ProfileUpdateSerializer(person, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
    return HttpResponse(status=401)


@api_view(['GET'])
def user_review(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    reviews = person.review_set.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def follow(request, username):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), username=username)
        if person != request.user:
            if person.follower.filter(username=request.user.username).exists():
                person.follower.remove(request.user)
                follow_state = False
            else:
                person.follower.add(request.user)
                follow_state = True
        data = {
            'follow_state': follow_state,
            'follow_count': person.follower.count(),
        }
        return JsonResponse(data=data, status=status.HTTP_200_OK)
    return HttpResponse(status=401)


@api_view(['POST'])
def account_delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    data = {
        'message': "회원정보가 삭제 되었습니다."
    }
    return JsonResponse(data=data, status=status.HTTP_204_NO_CONTENT)
    