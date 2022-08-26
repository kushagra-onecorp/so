
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def createPost_f(request):
    try:
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid():
            Description = serializer.data['Description'] if serializer.data['Description'] else ''
            FBDescription = serializer.data['FBDescription'] if serializer.data['FBDescription'] else ''
            InstaDescription = serializer.data['InstaDescription'] if serializer.data['InstaDescription'] else ''
            LinkedinDescription = serializer.data['LinkedinDescription'] if serializer.data['LinkedinDescription'] else ''
            Images = request.FILES.getlist('Images')
            UserToken = serializer.data['UserToken']
            Socials = serializer.data['Socials'].split(",")
            PagesId = serializer.data['PagesId'].split(",")
            # ! Get UserID from User Token
            userdata = get_user_q(UserToken)
            print('--Validating User Token---------')
            if not userdata:
                print('--Invalid User Token---------')
                json_data = {
                    'status_code': 200,
                    'status': 'fail',
                    'data': 'Invalid User Token, The token may have expired, You may need to re-login',
                    'message': 'Invalid User Token, The token may have expired, You may need to re-login'
                }
                return Response(json_data, status=stus.HTTP_200_OK)
            print('--Gettting User Id---------')
            UserId = userdata['UserId']
            CompanyId = userdata['CompanyId']
            print('--Managing Descriptions---------')
            if not Description or (len(FBDescription) <= 0):
                Description = ''
            if(len(FBDescription) <= 0):
                FBDescription = Description
            if(len(InstaDescription) <= 0):
                InstaDescription = Description
            if(len(LinkedinDescription) <= 0):
                LinkedinDescription = Description
            print('--Uploading Image---------')
            paths = []
            images = []
            for Image in Images:
                filedata = second_file_uploader(
                    Image, "social", f'post_image.jpg{Images.index(Image)}')
                path = '/home/ubuntu/Rashtradharma' + \
                    filedata['path']+'/'+filedata['fileName']
                img_url = 'https://promote.onecorp.co.in' + \
                    filedata['path']+'/'+filedata['fileName']
                paths.append(path)
                images.append(img_url)
            usercredentials = get_credentials_q(UserId)
            FacebookPosts = []
            LinkedinPosts = []
            InstagramPosts = []
            postData = {
                'is_post_done': []
            }
            detials = 0
            if usercredentials:
                for credential in usercredentials:
                    for id in PagesId:
                        if 'facebook' in Socials and credential['SocialMediaName'] == 'facebook' and credential['PageId'] == id:
                            print('--POSTING On Facebook---------')
                            detials = make_facebook_posts(
                                FBDescription, images, credential['SocialMediaAccessToken'], credential['PageId'])
                            if type(detials) == str:
                                FacebookPosts.append(
                                    {'postId': detials, 'credentialId': credential['CredentialId']})
                                print('--POSTED On Facebook---------')
                            else:
                                print('--NOT POSTED On Facebook---------')
                        elif 'instagram' in Socials and credential['SocialMediaName'] == 'instagram' and credential['PageId'] == id:
                            print('--POSTING On Instagram---------')
                            detials = make_instagram_posts(
                                InstaDescription, images, credential['SocialMediaAccessToken'], credential['PageId'])
                            if type(detials) == str:
                                InstagramPosts.append(
                                    {'postId': detials, 'credentialId': credential['CredentialId']})
                                print('--POSTED On Instagram---------')
                            else:
                                print('--NOT POSTED On Instagram---------')
                        elif 'linkedin' in Socials and credential['SocialMediaName'] == 'linkedin' and credential['PageId'] == id:
                            print('--Posting On Linkedin---------')
                            detials = make_linkedin_post(
                                credential['SocialMediaAccessToken'], LinkedinDescription, paths)
                            if type(detials) == str:
                                LinkedinPosts.append(
                                    {'postId': detials, 'credentialId': credential['CredentialId']})
                                print('--POSTED On Linkedin---------')
                            else:
                                print('--NOT POSTED On Linkedin---------')
                            print('--POST On Linkedin Done---------')

            # ! Get Facebook and LinkedIn Tokens from UserID
            print('--Calculating Posts---------')
            if(len(FacebookPosts) > 0):
                postData['is_post_done'].append('facebook')
            if(len(InstagramPosts) > 0):
                postData['is_post_done'].append('instagram')
            if(len(LinkedinPosts) > 0):
                postData['is_post_done'].append('linkedin')
            print('--Calculated Posts---------')
            print('*********', type(postData))
            print(
                '*********', list_convert(FacebookPosts, 'postId'))
            print(
                '*********', list_convert(InstagramPosts, 'postId'))
            print(
                '*********', list_convert(LinkedinPosts, 'postId'))
            # ! Save Post Using UserID
            # ? POST STATUS: 'Live','Scheduled','Draft'
            data = {
                "UserId": UserId,
                "CompanyId": CompanyId,
                "Title": "",
                "ImageUrl": ','.join(images),
                "Description": Description,
                "FBDescription": FBDescription,
                "InstaDescription": InstaDescription,
                "LinkedinDescription": LinkedinDescription,
                "IsInstaPost": '1' if 'instagram' in postData.get('is_post_done', '') else '0',
                "IsFBPost": '1' if 'facebook' in postData.get('is_post_done', '') else '0',
                "IsLinkedinPost": '1' if 'linkedin' in postData.get('is_post_done', '') else '0',
                "PostStatus": 'Live',
                "FacebookPostId": list_convert(FacebookPosts, 'postId'),
                "InstagramPostId":  list_convert(InstagramPosts, 'postId'),
                "LinkedinPostId": list_convert(LinkedinPosts, 'postId'),
                "ScheduleDate": 'NA',
                "ToPost": ','.join(Socials),
                "FacebookPageId": ','.join(PagesId),
                "IsDeleted": '0',
                "CreatedBy": 'system',
                "UpdatedBy": 'system',
                "CreatedAt": datetime.now(),
                "UpdatedAt": datetime.now()
            }
            print('*******', data)
            if len(postData.get('is_post_done', [])) > 0:
                print('--Saving To Database---------')
                print('---Saving Post---------')
                resp = SavePost_q(data.values())
                SocialId = get_post_by_pk_q(resp)['SocialId']
                print('---Saved Post---------')
                for post in FacebookPosts+InstagramPosts+LinkedinPosts:
                    data = {
                        "SocialId": SocialId,
                        "SocialPostId": post['postId'],
                        "CredentialId": post['credentialId'],
                        "IsDeleted": '0',
                        "CreatedBy": 'system',
                        "UpdatedBy": 'system',
                        "CreatedAt": datetime.now(),
                        "UpdatedAt": datetime.now()
                    }
                    print(
                        f'---Saving Post Detials for {post["postId"]}---------')
                    resp = SavePostDetials_q(data.values())
                    print('---Saved Post Detials---------')
                print('--Saved To Database---------')
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': "",
                    'message': f"Posted Successfully to {', '.join(postData.get('is_post_done','')).title()}",
                }
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': f"Not Posted!",
                    'message': f"Not Posted!"
                }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data)

