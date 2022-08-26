from social import make_facebook_posts, make_instagram_posts, make_linkedin_post

# Facebook
token="EAAUFRLCbo1MBAAZC8clT1dgYAeZAIT0ZAZCl6LQNGpZA97VRQs6ZCi5z79tmFIMfyHlxoR0VPDLRYBdzxbx7N1QyMdM7nDKmR3sE2ZBZAs5B3jfZCIHNQVfQ1S3tOQ7ZARxZCtsjiRkKLkccRLz38ZCrLmiBjR3CgNS6p1ZA8ibgJuA8qjACza3vWmi12"
description="Test Post Neww"
url=['https://wallpaperaccess.com/full/1398213.jpg',
     'https://wallpaperaccess.com/full/1398413.jpg',
     'https://wallpaperaccess.com/full/1398424.jpg',
     'https://wallpaperaccess.com/full/1398423.jpg',
     'https://wallpaperaccess.com/full/1396423.jpg',
     'https://wallpaperaccess.com/full/1388313.jpg',
     'https://wallpaperaccess.com/full/1386423.jpg',
     'https://wallpaperaccess.com/full/1386523.jpg',
     'https://wallpaperaccess.com/full/1386323.jpg']
page_id='102068252597979'

print(make_facebook_posts(description,url,token,page_id))


# Instagram
description="Test Post Neww"
page_id='17841453883347404'

print(make_instagram_posts(description,url,token,page_id))


# Linkedin
token="AQV27eAmEuBQMQEzeUVQgPRDcVeCRGePnrJbNf0vIKU6KRRXpAeL6tvHHi7YGMoKsYnvaA5ngptEJmInDOEil6Ye2kxxBCZME8nF5CdoPQLdij4mX7r5bTfsyQyS33UjEqV_9gUbGLnwR8vQQkl3BMqY8mqVnxTL9B_kyeKRX0DyDGYtbnXEVY9e5iKdmX4Wz7aHSpuZGB7_CfXJWvWauUpOwu5S2zZb6CYQAGjVqdmhJ2kUf8ADqC3KlwT4R0MdystXVaW1coBO5bqFjx3CRoE_u5U0F9MvY7ZzYwfI2I8lKlLT0tTjmCenMMs6Xw2YFuItEsGMiu7h-gmddADkjJXC-QGjHg"
description="Test Post Neww"
url=['./images/social.png',
     './images/post_image.jpg',
     './images/artronaut.jpg',
     './images/astrolight.jpg',
     './images/BATMAN.jpg',
     './images/home-bg.jpg',
     './images/KIWI.jpg',
     './images/person-girl.jpg',
     './images/WOOD.jpg']

print(make_linkedin_post(token,description,url))