# from typing_extensions import Required
from rest_framework import serializers



class Fileserializer(serializers.Serializer):
    MimeType = serializers.CharField(required = True)
    File = serializers.FileField(required = True)
    class Meta:
        fields = '__all__'



class FilesUrlerializer(serializers.Serializer):
    FilesUrl = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'


class SignupSerializer(serializers.Serializer):
    FirstName = serializers.CharField(required = True)
    LastName =  serializers.CharField(required=False, allow_blank=True,allow_null=True)
    Mobile = serializers.CharField(required = True)
    Email = serializers.CharField(required=False, allow_blank=True,allow_null=True)
    Password = serializers.CharField(required = True)
    ConfirmPassword = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'


class VerifyOTPSerializer(serializers.Serializer):
    Mobile = serializers.CharField(required = True)
    Otp = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'





class ThirdResendOTPSerializer(serializers.Serializer):
    Mobile = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'


class ResetPasswordSerializer(serializers.Serializer):
    Mobile = serializers.CharField(required = True)
    Otp = serializers.CharField(required= True)
    Password = serializers.CharField(required = True)
    ConfirmPassword = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'



class LoginSerializer(serializers.Serializer):
    Mobile = serializers.CharField(required = True)
    Password = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'

class AdhaarNoSerializer(serializers.Serializer):
    AdhaarNo = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'


class PanNoSerializer(serializers.Serializer):
    PanNo = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'



class GetSocialSerializers(serializers.Serializer):
    Title = serializers.CharField(required = True)
    Description = serializers.CharField(required = True)
    Image = serializers.FileField(required = True)
    LinkedinToken = serializers.CharField(required = True)
    FacebookToken = serializers.CharField(required = True)
    Socials = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'


class SocialUserSerializers(serializers.Serializer):
    UserName = serializers.CharField(required = True)
    AccessToken = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'


class GetSocialUserSerializers(serializers.Serializer):
    UserName = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'