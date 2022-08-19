

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def saveSocialCredentials_f(request):
    """_summary_
    Saves Credentials of user to the table
    Returns:
        Response
    """
    try:
        serializer = SaveCredentialsSerializer(data=request.data)
        if serializer.is_valid():
            FacebookCode = serializer.data["FacebookCode"]
            LinkedinCode = serializer.data["LinkedinCode"]
            UserToken = serializer.data["UserToken"]
            credentials = authenticate_social(LinkedinCode, FacebookCode)
            # ! Get UserID from User Token
            # ! Save Credentials using UserID
            json_data = {
                'status_code': 200,
                'status': 'Success',
                'data': "",
                'message': 'Saved Sucessfully',
            }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'data': serializer.errors,
                'message': 'Send Valid Data'
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
        raise APIException(json_data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def removeCredentials_f(request):
    try:
        serializer = RemoveCredentialsSerializer(data=request.data)
        if serializer.is_valid():
            UserToken = serializer.data["UserToken"]
            Social = serializer.data["Social"].split(",")
            # ! Get UserID from User Token
            # ! Get Credentials and update to isDeleted=1 from UserID
            json_data = {
                'status_code': 200,
                'status': 'Success',
                'data': "",
                'message': 'Removed Sucessfully',
            }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'data': serializer.errors,
                'message': 'Send valid data'
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
        raise APIException(json_data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def createPost_f(request):
    try:
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid():
            Title = serializer.data['Title']
            Description = serializer.data['Description']
            Image = request.FILES.get('Image')
            img_url = uploadImage(Image)
            UserToken = serializer.data['UserToken']
            Socials = serializer.data['Socials'].split(",")
            # ! Get UserID from User Token
            # ! Get Facebook and LinkedIn Tokens from UserID
            make_posts(FacebookToken, LinkedinToken, Title,
                       Description, path, img_url, Socials)
            # ! Save Post Using UserID
            json_data = {
                'status_code': 200,
                'status': 'Success',
                'data': "",
                'message': 'Posted Successfully',
            }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'data': serializer.errors,
                'message': 'Send valid data'
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
        raise APIException(json_data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def saveDraftPost_f(request):
    try:
        serializer = SaveDraftSerializer(data=request.data)
        if serializer.is_valid():
            Title = serializer.data['Title']
            Description = serializer.data['Description']
            Image = request.FILES.get('Image')
            img_url = uploadImage(Image)
            UserToken = serializer.data['UserToken']
            Socials = serializer.data['Socials'].split(",")
            # ! Get UserID from User Token
            # ! Save Post with Draft=1 using UserID
            json_data = {
                'status_code': 200,
                'status': 'Success',
                'data': "",
                'message': 'Saved Successfully',
            }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'data': serializer.errors,
                'message': 'Send valid data'
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
        raise APIException(json_data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def saveScheduledPost_f(request):
    try:
        serializer = SaveScheduledSerializer(data=request.data)
        if serializer.is_valid():
            Title = serializer.data['Title']
            Description = serializer.data['Description']
            DateTime = serializer.data['DateTime']
            Image = request.FILES.get('Image')
            img_url = uploadImage(Image)
            UserToken = serializer.data['UserToken']
            Socials = serializer.data['Socials'].split(",")
            # ! Get UserID from User Token
            # ! Save Post with Scheduled=1 and Time using UserID
            json_data = {
                'status_code': 200,
                'status': 'Success',
                'data': "",
                'message': 'Scheduled Successfully',
            }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'data': serializer.errors,
                'message': 'Send valid data'
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
        raise APIException(json_data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getPosts_f(request):
    try:
        serializer = GetPostSerializer(data=request.data)
        if serializer.is_valid():
            UserToken = serializer.data['UserToken']
            # ! Get UserID from User Token
            # ! Get Posts from UserID
            posts = {}
            json_data = {
                'status_code': 200,
                'status': 'Success',
                'data': posts,
                'message': 'Found Successfully',
            }
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'data': serializer.errors,
                'message': 'Send valid data'
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
        raise APIException(json_data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def GetCredentials_f(request):
    try:
        serializer = GetCredentialsSerializer(data=request.data)
        if serializer.is_valid():
            UserToken = serializer.data['UserToken']
            # ! Get UserID from User Token
            # ! Get Credentials from UserID
            credentials = {}
            json_data = {
                'status_code': 200,
                'status': 'Success',
                'data': credentials,
                'message': 'Found Successfully',
            }
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'data': serializer.errors,
                'message': 'Send valid data'
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
        raise APIException(json_data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def deletePost_f(request):
    try:
        serializer = DeletePostSerializer(data=request.data)
        if serializer.is_valid():
            UserToken = serializer.data["UserToken"]
            PostID = serializer.data["PostID"]
            # ! Get UserID from User Token
            # ! Get Post and update to isDeleted=1 from PostID
            json_data = {
                'status_code': 200,
                'status': 'Success',
                'data': "",
                'message': 'Removed Sucessfully',
            }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'data': serializer.errors,
                'message': 'Send valid data'
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
        raise APIException(json_data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def updatePost_f(request):
    try:
        serializer = UpdatePostSerializer(data=request.data)
        if serializer.is_valid():
            Title = serializer.data['Title']
            Description = serializer.data['Description']
            DateTime = serializer.data['DateTime']
            Image = request.FILES.get('Image')
            UserToken = serializer.data['UserToken']
            Socials = serializer.data['Socials'].split(",")
            PostID = serializer.data["PostID"]
            img_url = uploadImage(Image)
            # ! Get UserID from User Token
            # ! Get Post from PostID
            # ! Update Pos
            json_data = {
                'status_code': 200,
                'status': 'Success',
                'data': "",
                'message': 'Updated Sucessfully',
            }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'data': serializer.errors,
                'message': 'Send valid data'
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
        raise APIException(json_data)
