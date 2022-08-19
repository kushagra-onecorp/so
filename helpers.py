def uploadImage(Image):
    filedata = second_file_uploader(Image, "social", 'post_image.jpg')
    path = '/home/ubuntu/rzrozgaarindia' + \
        filedata['path']+'/'+filedata['fileName']
    img_url = 'https://api-preview.rozgaarindia.com' + \
        filedata['path']+'/'+filedata['fileName']
    print(path)
    return img_url