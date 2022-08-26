
class CreatePostSerializer(serializers.Serializer):
    """_summary_

    Args:
        User Token, Title,Description,FBDescription,InstaDescription,LinkedinDescription,Image,Socials,PagesId
    """
    Description = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    FBDescription = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    LinkedinDescription = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    InstaDescription = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    Images = serializers.FileField(required=True)
    UserToken = serializers.CharField(required=True)
    Socials = serializers.CharField(required=True)
    PagesId = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)

    class Meta:
        fields = '__all__'
