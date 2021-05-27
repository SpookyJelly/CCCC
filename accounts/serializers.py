from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
	


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password1','password2','groupcolor','introduction','profileimage')
        extra_kwargs = {'password1': {'write_only': True}, 'password2': {'write_only': True}, 'following':{'read_only':True}}
        

class ProfileSerializer(UserSerializer):

     class Meta:
         model = User
         fields = ('username','groupcolor','introduction','profileimage','review_set','following','follower')


class ProfileUpdateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('username','groupcolor','introduction','profileimage')
        extra_kwargs = {'username':{'read_only':True}}


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','groupcolor')


from allauth.account.adapter import get_adapter


class CustomRegisterSerializer(RegisterSerializer, UserSerializer):

    email = None

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'groupcolor': self.validated_data.get('groupcolor', ''),
            'introduction': self.validated_data.get('introduction', ''),
            'profileimage': self.validated_data.get('profileimage', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        user.groupcolor = self.cleaned_data.get('groupcolor', '')
        user.introduction = self.cleaned_data.get('introduction', '')
        user.profileimage = self.cleaned_data.get('profileimage', '')
        user.save()
        self.custom_signup(request, user)
        return user
        

class CustomLoginSerializer(LoginSerializer):
    
    email = None


