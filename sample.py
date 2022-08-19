# !! Serializer
class GetSocialSerializers(serializers.Serializer):
    Title = serializers.CharField(required=True)
    Description = serializers.CharField(required=True)
    Image = serializers.FileField(required=True)
    LinkedinCode = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'

# !! View


@api_view(['POST'])
# @authentication_classes((TokenAuthentication,))
# # @permission_classes((IsAuthenticated,))
def GetSocialData(request):
    try:
        serializer = GetSocialSerializers(data=request.data)
        if serializer.is_valid():
            Title = serializer.data['Title']
            Description = serializer.data['Description']
            Image = request.FILES.get('Image')
            LinkedinCode = serializer.data['LinkedinCode']
            make_posts(LinkedinCode, Title, Description)
            json_data = {
                'status_code': 200,
                'status': 'Success',
                'data': "",
                'message': 'Posted Sucessfully',
            }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'data': serializer.errors,
                'message': ' Send valid data  '
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        return Response(json_data, status=stus.HTTP_400_BAD_REQUEST)

# !! Querry


def Insertfreejobalert_q(data):
    with connections['Freelancer'].cursor() as cursor:
        resp = cursor.execute(""" INSERT INTO dbfreelancersecond.JobAlert
                (
                JAUUid,
                FUserId,
                FUserName,
                IsDeleted,
                CreatedAt,
                CreatedBy,
                UpdatedAt,
                UpdatedBy)
                VALUES
                (UUID(),%s,%s,%s,%s,%s,%s,%s); """, data)
        resp = cursor.lastrowid
        return resp
