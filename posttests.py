from blog.models import Post
from django.contrib.auth.models import User

me = User.objects.get(username='daeun')
Post.objects.create(author=me, title='Sample title', text='Test')

Post.objects.all()