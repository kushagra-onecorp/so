class SaveCredentialsSerializer(serializers.Serializer):
    """_summary_

    Args:
        FacebookCode,LinkedinCode,UserToken
    """
    FacebookCode = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    LinkedinCode = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    UserToken = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'


class RemoveCredentialsSerializer(serializers.Serializer):
    """_summary_

    Args:
        User Token, Soical String
    """
    UserToken = serializers.CharField(required=True)
    Scoials = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'


class CreatePostSerializer(serializers.Serializer):
    """_summary_

    Args:
        User Token, Title,Description,Image,Socials
    """
    Title = serializers.CharField(required=True)
    Description = serializers.CharField(required=True)
    Image = serializers.FileField(required=True)
    UserToken = serializers.CharField(required=True)
    Socials = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'


class SaveDraftSerializer(serializers.Serializer):
    """_summary_

    Args:
        User Token, Title,Description,Image,Socials
    """
    Title = serializers.CharField(required=True)
    Description = serializers.CharField(required=True)
    Image = serializers.FileField(required=True)
    UserToken = serializers.CharField(required=True)
    Socials = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'


class SaveScheduledSerializer(serializers.Serializer):
    """_summary_

    Args:
        User Token, Title,Description,Image,Socials,Time to post
    """
    Title = serializers.CharField(required=True)
    Description = serializers.CharField(required=True)
    Image = serializers.FileField(required=True)
    UserToken = serializers.CharField(required=True)
    Socials = serializers.CharField(required=True)
    DateTime = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'


class GetPostsSerializer(serializers.Serializer):
    """_summary_

    Args:
        User Token
    """
    UserToken = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'


class GetCredentialsSerializer(serializers.Serializer):
    """_summary_

    Args:
        User Token
    """
    UserToken = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'


class DeletePostSerializer(serializers.Serializer):
    """_summary_

    Args:
        User Token,Post Id
    """
    UserToken = serializers.CharField(required=True)
    PostID = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'


class UpdatePostSerializer(serializers.Serializer):
    """_summary_

    Args:
        User Token,Post ID, Title,Description,Image,Socials
    """
    Title = serializers.CharField(required=True)
    Description = serializers.CharField(required=True)
    Image = serializers.FileField(required=True)
    UserToken = serializers.CharField(required=True)
    PostID = serializers.CharField(required=True)
    Socials = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'
