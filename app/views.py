from xml.dom.minidom import Document
from django.shortcuts import render
from .serializers import *
from .queries import *
from .helper import *
# Create your views here.
import razorpay
from django.shortcuts import render
from django.http import HttpResponse
import hashlib
# Create your views here.
# from .serializer import *
# from .queries import *
from django.views.decorators.csrf import csrf_exempt
# from .helper import *
from rest_framework.exceptions import APIException
import sys, random, hashlib, json, datetime, uuid, socket, time, os, inspect
from rest_framework.response import Response
import urllib.request

from django.shortcuts import render
from rest_framework.response import Response
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status as stus
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from django.db import connection, transaction
from django.core.paginator import Paginator
import sys, random, hashlib, json, time, requests, urllib,unicodedata
#import xmltodict

from random import randint, randrange,choice
from datetime import datetime

from django.conf import settings

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
import pickle
from .social import *

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def fileconvert_f(request):
    try:
        print("gggmm")
        print(request)
        serializer = Fileserializer(data = request.data)
        print("nnn")
        if serializer.is_valid():
            print("kkkk")
            files = request.FILES.get('File')
            print("lllll")
            fiepath = second_file_uploader(files,'123',files)
            print(type(fiepath))
            # print('vvvvvvvv')
            data1 = []
            path = "/home/ubuntu/rzrozgaarindia"+fiepath['path']+'/'+fiepath['fileName']
            import base64
            # file1 = open(path, "rb")
            # v=file1.read()
            print(open(path, 'rb').read())
            c = base64.b64encode(open(path, 'rb').read())
            print(c)
            temp=str(time.time())
            extention =  str(files.name).split(".")
            newtemp = temp.split('.')
            name = newtemp[0]+"."+extention[-1]
            path_base64 = '/home/ubuntu/rzrozgaarindia/rzstatic/ai/base64'+'/'+str(name)
            dirName = '/home/ubuntu/rzrozgaarindia/rzstatic/ai/base64'
            # print('kkkk',path_base64)
            if not os.path.isdir(dirName):
                os.makedirs(dirName)
            f = open(path_base64, 'w+')
            print('mmmmmmmmm')
            f.write(str(c.decode()))
            f.close()
            fdata = open(path_base64, 'r+')
            pdfbase64data = fdata.read()
            # print(pdfbase64data)
            fdata.close()
            url = "https://us-documentai.googleapis.com/v1/projects/834036704623/locations/us/processors/33a7ee7212d2a6d:process?access_token=ya29.c.b0AXv0zTOXzUKMDtFvoFl76cn67w7wDVvTy1HtM_LwMmLrNlCm1BB7oXmkfpLjXQv8d50JMpX8pRAwyCBiAC3Xm5ISti6-I0D44qFQltW_OV4_DzBU-cFambjKqAQOe0MRvrU_J_oYOYK4v4bym2oR6w6_91xFp2_eQUSO_YGHLiANRrYcHaF3RNkqW64quVk0M40NVkUnIEW71OB2Q-d3ofGptuJ3mQ"
            payload = json.dumps({
            "skipHumanReview": "false",
            "rawDocument": {
                "mimeType":serializer.data['MimeType'],
                "content":pdfbase64data
            },
            "fieldMask":"text,entities,pages.pageNumber,user.displayName,photo"
            })
            headers = {
                'Content-Type': 'application/json'
                }
            response = requests.request("POST", url, headers=headers, data=payload)
            import re
            cccc = json.loads(response.text)
            print(cccc)
            obj=re.compile(r"[0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9][0-9]")
            x = obj.match( cccc.get('document').get('text'))
            pp = re.findall(r"\s[0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9][0-9]", cccc.get('document').get('text'))
            pancard = re.findall(r"[A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][A-Z]", cccc.get('document').get('text'))
            splitdata = response.text.split("Your Aadhaar No. :")
            print(splitdata,"ooooooooo")
            regx = "^[2-9]{1}[0-9]{3}\\"+"s[0-9]{4}\\s[0-9]{4}$"
            p = re.compile(regx)
            print(p,"jjjjjjjjjjj")
            fff = re.match(regx, cccc.get('document').get('text'))
            print(fff,"LLLLLLLLLLLL")
            # pp = re.findall(r"^[2-9]{1}[0-9]{3}\\" +"s[0-9]{4}\\s[0-9]{4}$", cccc.get('document').get('text'))
            print(x,'==================>',pp)
            pr = ""
            da=json.loads(response.text)
            adhar = ""
            if pp:
                adhar = pp[0][1:]
            pdata = ""
            if pancard:
                pdata = pancard[0]
            print(da,'????')
            if cccc.get('document'):
                # fdata = json.loads(da)
                # print(da.get('document').get('text'))
                json_data = {
                    'status_code' : 200,
                    'status': 'Success',
                    'data':da.get('document').get('text'),
                    'Aadhaar':adhar,
                    'Pan':pdata,
                    'message': 'data found',
                }
                return Response(json_data, status= stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code' : 200,
                    'status': 'Success',
                    'data':'',
                    'message': 'data not found',
                }
                return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'data': serializer.errors,  
                'message': ' Send valid data  '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        return Response(json_data, status= stus.HTTP_400_BAD_REQUEST)



    
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def accetoken_f(request):
    try:

        import requests
        import requests.auth
        print('jjskfd')
        CLIENT_ID = "834036704623-tr39vdms2kpic3e0had536adik2dg3pn.apps.googleusercontent.com"
        CLIENT_SECRET = "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"
        TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
        REDIRECT_URI = "https://www.getpostman.com/oauth2/callback"
        client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
        post_data = {"grant_type": "client_credentials",
                        "code": 'Bearer',
                        "redirect_uri":REDIRECT_URI}
        response = requests.post(TOKEN_URL,
                                    auth=client_auth,
                                    data=post_data)
        token_json = response.json()
        print(token_json)
        print(token_json["access_token"])
        # url = "https://us-documentai.googleapis.com/v1/projects/834036704623/locations/us/processors/33a7ee7212d2a6d:process"
        # response = requests.post(
        # url,
        # data={"grant_type": "client_credentials"},
        # auth=(CLIENT_ID, CLIENT_SECRET),)
        # print(response.json())
        # response.json()["access_token"]
        data = []
        if type(data)==list:
            json_data = {
                'status_code' : 200,
                'status': 'Success',
                'data':response.text,
                'message': 'data found',
            }
            return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 200,
                'status': 'Success',
                'data':'',
                'message': 'data not found',
            }
            return Response(json_data, status= stus.HTTP_200_OK)
    except Exception as e:
        print("Error --------:",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        return Response(json_data, status= stus.HTTP_400_BAD_REQUEST)










# @api_view(['POST'])
# @authentication_classes((TokenAuthentication,))
# @permission_classes((IsAuthenticated,))
@csrf_exempt
def docApi_f(request):
    try:

        f = open('/home/ubuntu/rzrozgaarindia/rzstatic/aitest.txt', 'w+')
        f.write("ssss"+str(request))
        data = request.body
        f.write(data)
        f.close()
        data = []
        if type(data)==list:
            json_data = {
                'status_code' : 200,
                'status': 'Success',
                'data':data,
                'message': 'data found',
            }
            return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 200,
                'status': 'Success',
                'data':'',
                'message': 'data not found',
            }
            return Response(json_data, status= stus.HTTP_200_OK)
    except Exception as e:
        f = open('/home/ubuntu/rzrozgaarindia/rzstatic/aitest.txt', 'a+')
        f.write(str(e))
        f.close()
        print("Error --------:",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        return Response(json_data, status= stus.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def aigoogleauthcall_f(request):
    try:
        from django.http import HttpResponseRedirect
        token_request_uri = "https://accounts.google.com/o/oauth2/auth"
        response_type = "code"
        client_id = "834036704623-tr39vdms2kpic3e0had536adik2dg3pn.apps.googleusercontent.com"
        redirect_uri = "https://api-preview.rozgaarindia.com/api/AiApp/docAi"
        scope = "https://www.googleapis.com/auth/cloud-platform"
        url = "{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}".format(
        token_request_uri = token_request_uri,
        response_type = response_type,
        client_id = client_id,
        redirect_uri = redirect_uri,
        scope = scope)
        resp = requests.get(url)
        print("api successfully call",resp)
        # return HttpResponseRedirect(url)
        data = []
        if type(data)==list:
            json_data = {
                'status_code' : 200,
                'status': 'Success',
                'data':resp.json(),
                'message': 'data found',
            }
            return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 200,
                'status': 'Success',
                'data':'',
                'message': 'data not found',
            }
            return Response(json_data, status= stus.HTTP_200_OK)
    except Exception as e:
        f = open('/home/ubuntu/rzrozgaarindia/rzstatic/aitest.txt', 'a+')
        f.write(str(e))
        f.close()
        print("Error --------:",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        return Response(json_data, status= stus.HTTP_400_BAD_REQUEST)



#=============================================================
# Send-OTP-By-SMS
def SendSMSOtp(mobile):
    try:
        # sending otp
        otp = random.randint(1000,9999)
        message = f'Your one time password (OTP) to complete your account verification at Rozgaar India is - {otp}. OTP is confidential, do not share it with anyone.'
        if sendOTP(mobile, message):
            return otp
        else:
            return None
    # exception response
    except Exception as e:
        print(e)
# ===============================================================

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def usersignup_f(request):
    try:
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid():
            userdata = getuserbymobile_q(serializer.data['Mobile'])
            if userdata==None:
                if serializer.data['Password']==serializer.data['ConfirmPassword'] and len(serializer.data['Password'] if serializer.data['Password'] else "")>0:
                    data = {'FirstName':serializer.data['FirstName'],
                            'LastName':serializer.data['LastName'],
                            'UserName':UniqueUserNameGenerator(serializer.data['FirstName'],serializer.data['LastName']),
                            'Mobile':serializer.data['Mobile'],
                            'Email':serializer.data['Email'] if serializer.data['Email'] else str(serializer.data['Mobile'])+'@rozgaarindia.com',
                            'Password':hashlib.md5(str(serializer.data['Password']).encode()).hexdigest(),
                            'IsDeleted':"0",
                            'created_at': datetime.now(),
                            'updated_at': datetime.now(),
                            'created_by': 'System',
                            'Updated_by': 'System'
                        }
                    #Extracting Values from the dictionary
                    datatemp = data.values()
                    print("dafgsdg")
                    #Check if Confirm password and Password is matched
                    
                    data = UserSignupQuery_q(datatemp)
                    # data = GetAllUserName_q()
                    print("hhgg",data)
                    # Send OTP on SMS if User from india
                    
                    emailstatus = 'OTP has been sent by sms'
                    otp = SendSMSOtp(serializer.data['Mobile'])
                    if otp:
                        pass
                    else:
                        print(otp,'323233232323')
                        json_data = {
                        'status_code' : 300,
                        'status': 'fail',
                        'data':'',
                        'OtpStatus':'otp not send',
                        'message': 'otp not send',
                        }
                        return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)   
                    #print("MY send otp is :",otp)
                    if otp==None:
                        emailstatus='OTP is not send'
                    #Inserting opt with user UserId
                    insertotpintodb =[
                        str(data['UserId']),
                        serializer.data['Mobile'],
                        serializer.data['Email'] if serializer.data['Email'] else data['Email'],
                        otp,
                        datetime.now(),
                        1,
                        datetime.now(), 
                    ]
                    lid = InsertOTPdata_q(insertotpintodb)
                    json_data = {
                        'status_code' : 200,
                        'status': 'SUCCESS',
                        'data':replace_null_with_empty_string(data),
                        'message': 'Data successfully created',
                    }
                    return Response(json_data, status= stus.HTTP_200_OK)
                else:
                    json_data = {
                        'status_code' : 200,
                        'status': 'FAILED',
                        'data':'Data is not saved.',
                        'message': 'Both Password should be matched',
                    }
                    return Response(json_data, status= stus.HTTP_200_OK)
            else:
                    json_data = {
                        'status_code' : 200,
                        'status': 'FAILED',
                        'data':'User already exist',
                        'message': 'Mobile already exixt',
                    }
                    return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'data': serializer.errors,  
                'message': 'data not found '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error :",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'Reason':e,
            'Remarks': 'landed in exception'
        }
        raise APIException(json_data)





# Verify OTP start--------------------------------------------------------------------------
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def VerifyOtp_f(request):
    try:
        serializer = VerifyOTPSerializer(data = request.data)
        if serializer.is_valid():
            
            print("----+++++++++++++++++++++++++++++++++++++-------------------------------------")
            rdata = VerifyOtpofuser_q(serializer.data['Mobile'])
            if rdata:
                if rdata['Otp'] == serializer.data['Otp']:
                    print("Otp is INDia------------------")
                    data = {
                    'varifiedStatus':1,
                    'Mobile':serializer.data['Mobile'],
                    'Otp':rdata['Otp'],
                    }
                    rdata = UpdateOtpVerification_q(data.values(),serializer.data['Mobile'])
                    resdata = getuserbymobile_q(serializer.data['Mobile'])
                    json_data = {
                        'status_code' : 200,
                        'status': 'SUCCESS',
                        'data':replace_null_with_empty_string(resdata),
                        'message': 'Data has been saved successfully!',
                    }
                    return Response(json_data, status= stus.HTTP_200_OK)
                
                else:
                    json_data = {
                        'status_code' : 200,
                        'status': 'FAILED',
                        'data':'Otp Not Matched',
                        'message': 'Please Enter Correct OTP',
                    }
                    return Response(json_data, status= stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code' : 200,
                    'status': 'FAILED',
                    'data':'',
                    'message': 'Please Enter Valid Mobile Number',
                }
                return Response(json_data, status= stus.HTTP_200_OK)
           
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'data': serializer.errors,  
                'message': 'data not found '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error :",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        return Response(json_data, status= stus.HTTP_400_BAD_REQUEST)

# Verify OTP start End--------------------------------------------------------------------------






@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def resendOtp_f(request):
    try:
        serializer = ThirdResendOTPSerializer(data = request.data)
        if serializer.is_valid():
            userinfo = getuserbymobile_q(serializer.data['Mobile'])
            if userinfo:
                # Send OTP on SMS if User from india
                if serializer.data['Mobile']:
                    otp = SendSMSOtp(serializer.data['Mobile'])
                    if otp:
                        pass
                    else:
                        json_data = {
                            'status_code' : 200,
                            'status': 'Fail',  
                            'message': 'OTP Not send'
                        }
                        return Response(json_data, status= stus.HTTP_200_OK)
                    #Inserting opt with user UserId
                    insertotpintodb =[
                        str(userinfo['UserId']),
                        serializer.data['Mobile'],
                        userinfo['Email'],
                        otp,
                        datetime.now(),
                        1,
                        datetime.now(), 
                    ]
                    lid = InsertOTPdata_q(insertotpintodb)
                    json_data = {
                        'status_code' : 200,
                        'status': 'SUCCESS',
                        'data':userinfo,
                        'message': 'OTP sent successfully',
                    }
                    return Response(json_data, status= stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code' : 300,
                    'status': 'fail',  
                    'Reason': 'Please Enter Valid Mobile',
                    'Remark': 'Mobile Invalid'
                }
                return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
        # serializer Error
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'Reason': serializer.errors,  
                'Remark': 'Serializer Error '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error :",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'Reason':e,
            'Remarks': 'landed in exception'
        }
        raise APIException(json_data)



@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def resetPassword_f(request):
    try:
        serializer = ResetPasswordSerializer(data = request.data)
        if serializer.is_valid():
            rdata = VerifyOtpofuser_q(serializer.data['Mobile'])
            if rdata:
                if rdata['Otp'] == serializer.data['Otp']:
                    if serializer.data['Password']==serializer.data['ConfirmPassword'] and len(serializer.data['Password'] if serializer.data['Password'] else "")>0:
                        Password=hashlib.md5(str(serializer.data['Password']).encode()).hexdigest(),
                        rdata = Updatepassword_q(Password,serializer.data['Mobile'])
                        rdata = getuserbymobile_q(serializer.data['Mobile'])
                        json_data = {
                        'status_code' : 200,
                        'status': 'SUCCESS',
                        'data':rdata,
                        'message': 'Password change successfully',
                        }
                        return Response(json_data, status= stus.HTTP_200_OK)
                    else:
                        json_data = {
                            'status_code' : 200,
                            'status': 'FAILED',
                            'data':'Data is not saved.',
                            'message': 'Both Password should be matched',
                        }
                        return Response(json_data, status= stus.HTTP_200_OK)
                else:
                    json_data = {
                        'status_code' : 200,
                        'status': 'FAILED',
                        'data':'Otp Not Matched',
                        'message': 'Please Enter Correct OTP',
                    }
                    return Response(json_data, status= stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code' : 200,
                    'status': 'FAILED',
                    'data':'',
                    'message': 'Please Enter Valid Mobile Number',
                }
                return Response(json_data, status= stus.HTTP_200_OK)
                    
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'Reason': serializer.errors,  
                'Remark': 'Serializer Error '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error :",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'Reason':e,
            'Remarks': 'landed in exception'
        }
        raise APIException(json_data)





@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def login_f(request):
    try:
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            mobile = serializer.data['Mobile']
            Password=hashlib.md5(str(serializer.data['Password']).encode()).hexdigest()
            data = getuserbymobileandPassword_q(mobile,Password)
            if type(data)==dict:
                json_data = {
                    'status_code' : 200,
                    'status': 'SUCCESS',
                    'data':replace_null_with_empty_string(data),
                    'message': 'data found successfully',
                }
                return Response(json_data, status= stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code' : 200,
                    'status': 'FAILED',
                    'data':'',
                    'message': 'no data found',
                }
                return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'Reason': serializer.errors,  
                'Remark': 'Serializer Error '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error :",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'Reason':e,
            'Remarks': 'landed in exception'
        }
        raise APIException(json_data)






@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def validateadhaar_f(request):
    try:
        serializer = AdhaarNoSerializer(data = request.data)
        if serializer.is_valid():
            url = "https://api.apiclub.in/api/v1/validate_aadhar"
            body = {"aadhar_no":serializer.data['AdhaarNo']}
            header = {"API-KEY":"417d574f4873825dc4cc9b11985a649a","Referer":"65.1.114.250","Content-Type":"application/json"}
            rresponse  = requests.post(url,headers = header,json = body )
            print(rresponse.json())
            if type(rresponse.json())==dict:
                json_data = {
                    'status_code' : 200,
                    'status': 'SUCCESS',
                    'data':rresponse.json(),
                    'message': 'data found successfully',
                }
                return Response(json_data, status= stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code' : 200,
                    'status': 'FAILED',
                    'data':'',
                    'message': 'no data found',
                }
                return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'Reason': serializer.errors,  
                'Remark': 'Serializer Error '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error :",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'Reason':e,
            'Remarks': 'landed in exception'
        }
        raise APIException(json_data)



@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def validatepan_f(request):
    try:
        serializer = PanNoSerializer(data = request.data)
        if serializer.is_valid():
            url = "https://api.apiclub.in/api/v1/verify_pan"
            body = {"pan_no":serializer.data['PanNo']}
            header = {"API-KEY":"417d574f4873825dc4cc9b11985a649a","Referer":"65.1.114.250","Content-Type":"application/json"}
            rresponse  = requests.post(url,headers = header,json = body )
            print(rresponse.json())
            if type(rresponse.json())==dict:
                json_data = {
                    'status_code' : 200,
                    'status': 'SUCCESS',
                    'data':rresponse.json(),
                    'message': 'data found successfully',
                }
                return Response(json_data, status= stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code' : 200,
                    'status': 'FAILED',
                    'data':'',
                    'message': 'no data found',
                }
                return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'Reason': serializer.errors,  
                'Remark': 'Serializer Error '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error :",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'Reason':e,
            'Remarks': 'landed in exception'
        }
        raise APIException(json_data)




@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def SendURL_f(request):
    linkedin_auth_url=send_url()
    try:
        rdata = {
            'authURL':linkedin_auth_url
        }
        json_data = {
                'status_code' : 200,
                'status': 'Success',
                'data':rdata,
                'message': '',
            }
        return Response(json_data, status= stus.HTTP_200_OK)
    except Exception as e:
        print("Error --------:",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        return Response(json_data, status= stus.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def GetSocialData_f(request):
    try:
        serializer =GetSocialSerializers(data = request.data)
        if serializer.is_valid():
            Title = serializer.data['Title']
            Description = serializer.data['Description']
            Image = request.FILES.get('Image')
            filedata = second_file_uploader(Image,"social",'post_image.jpg')
            path  = '/home/ubuntu/rzrozgaarindia'+filedata['path']+'/'+filedata['fileName']
            img_url  = 'https://api-preview.rozgaarindia.com'+filedata['path']+'/'+filedata['fileName']
            print(path)
            LinkedinToken = serializer.data['LinkedinToken']
            FacebookToken = serializer.data['FacebookToken']
            Socials = serializer.data['Socials'].split(",")
            print('dsssgggggggg')
            make_posts(FacebookToken,LinkedinToken,Title,Description,path,img_url,Socials)
            json_data = {
                    'status_code' : 200,
                    'status': 'Success',
                    'data':"",
                    'message': 'Posted Successfully',
                }
            return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'data': serializer.errors,  
                'message': ' Send valid data  '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        raise APIException(json_data)




@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def saveSocialuser_f(request):
    try:
        serializer =SocialUserSerializers(data = request.data)
        if serializer.is_valid():
            AccessToken = serializer.data['AccessToken']
            UserName = serializer.data['UserName']
            data = {'UserName':UserName,
                    'AccessToken':AccessToken,
                    "CreatedAt":datetime.now(),
                    'UpdatedAt':datetime.now()
                    }
            rdata = InsertsocialUser_q(data.values())
            json_data = {
                    'status_code' : 200,
                    'status': 'Success',
                    'data':rdata,
                    'message': 'Data save Successfully',
                }
            return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'data': serializer.errors,  
                'message': ' Send valid data  '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        return Response(json_data, status= stus.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def GetSocialuser_f(request):
    try:
        serializer =GetSocialUserSerializers(data = request.data)
        if serializer.is_valid():
            UserName = serializer.data['UserName']
            rdata = getsocialuse_q(UserName)
            if type(rdata)==dict:
                json_data = {
                        'status_code' : 200,
                        'status': 'Success',
                        'data':rdata,
                        'message': 'Data save Successfully',
                    }
                return Response(json_data, status= stus.HTTP_200_OK)
            else:
                json_data = {
                        'status_code' : 200,
                        'status': 'Success',
                        'data':'',
                        'message': 'Data not found',
                    }
                return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code' : 300,
                'status': 'fail',
                'data': serializer.errors,  
                'message': ' Send valid data  '
            }
            return Response(json_data, status= stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        return Response(json_data, status= stus.HTTP_400_BAD_REQUEST)







@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def Getcode_f(request):
    try:
        from ensurepip import version
        from google.oauth2 import service_account
        import google.auth.transport.requests
        import time

        SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin']
        SERVICE_ACCOUNT_FILE = '/home/ubuntu/rzrozgaarindia/rzstatic/assets/2022/07/14/1657793769.json'

        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES )



        # # # request = google.auth.transport.requests.Request()
        # # # kk = credentials.refresh(request)
        # # oo = credentials.with_always_use_jwt_access(credentials)
        # # print("lllllll---2222-------- ",oo)

        # import time

        from oauth2client.service_account import ServiceAccountCredentials
        # The scope for the OAuth2 request.
        SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

        # The location of the key file with the key data.
        KEY_FILEPATH = SERVICE_ACCOUNT_FILE

        # Defines a method to get an access token from the ServiceAccount object.
        def get_access_token():
            return ServiceAccountCredentials.from_json_keyfile_name(
            KEY_FILEPATH, SCOPE).get_access_token().access_token

        print("My Access Token --- ",get_access_token())
        # resp = requests.get(url)
        # print(resp.text)
        rdata=[]
        if type(rdata)==dict:
            json_data = {
                    'status_code' : 200,
                    'status': 'Success',
                    'data':'',
                    'message': 'Data save Successfully',
                }
            return Response(json_data, status= stus.HTTP_200_OK)
        else:
            json_data = {
                    'status_code' : 200,
                    'status': 'Success',
                    'data':'',
                    'message': 'Data not found',
                }
            return Response(json_data, status= stus.HTTP_200_OK)
    except Exception as e:
        print("Error --------:",e)
        json_data = {
            'status_code' : 400,
            'status': 'Fail',
            'data': e,
            'message': 'landed in exception',
        }
        return Response(json_data, status= stus.HTTP_400_BAD_REQUEST)


# ==========API Document ====================================================







