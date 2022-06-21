from django.db import models

class Post(models.Model):
    titles = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)
    ''' 
    이 부분이 없으면 게시글 제목이 나오지 않고 Post object(1), (2)로 나온다.
    '''
    def __str__(self):
        return self.titles
    
    
