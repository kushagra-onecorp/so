from social import authenticate_social, make_facebook_posts, make_instagram_posts, make_linkedin_post
def makePosts():
     # Facebook
     token="EAALefOGyJXQBAMzYOn9J60TmHylZA02B8YbsZCaxSesYlYrW0fpb0aXtr3sUvc8TZAU2HEijrhcy1UsZBXcVP1ck0EjVEYuHdgnffgvsGuQ06onNqPonnxdBZC3uz0V8LKhEgBn0GEvZBZAIF7BiBBkKLQC2CTx0JXm1ZAeJ4IdwJZBELrnlUdinsrQnP7LOdxG4w0uZCIqEyPdYZBeiVX14eEkWiizH0s9Lb9gDtFZCMwXI2OkyBfcxaeDCZAMXsYgs4O0ZD"
     description="Test Post Neww"
     url=['https://wallpaperaccess.com/full/1398213.jpg']
     page_id='102068252597979'

     # print(make_facebook_posts(description,url,token,page_id))

     # Instagram
     description="Test Post Neww"
     page_id='17841416005675720'

     # print(make_instagram_posts(description,url,token,page_id))


     # Linkedin
     token="AQUqQKZJxz97WHgCmz_CEckhGv7HTj_3xpQR_5RgS-QdXkt8EV50XboCmXqw_h67adWQgXFFlAzDoA7bp5LjOaD-0JMXJ9xFZoP9aGhRv_MsWhXzFV83R2c8wV2H8cKu9BkgpVEoRqgOzTZi00AyXyjGWNjuuZGy6fhMKkCYp2vdJ2q3ifgS5vT22LlkjU2Gk78lyf6sqKHFbV8sXOpu3CB1DdRxWNKqMle87IHATeO4b4faGDmlCIgzlwlCOnxT1XV02orBPPvEJFk7XyI9o4sne-ITmqkbZ7Ji0kiATqbm0wiKbQHA5yWS_D-7pj3WCabaqIrZLYNJNDrSUjq90QLpexZdWg"
     url=['./images/social.png']

     print(make_linkedin_post(token,description,url))
     
def Authenticate():
     codeFB=input('FBCode:')
     codeLink=input('LinkedinCode:')
     print(authenticate_social(codeLink,codeFB))
     
makePosts()