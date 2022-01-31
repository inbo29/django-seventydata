from django.db import models


# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    # makemigrations -> migrate
    class Meta:
        ordering = ['-updated']  # - 면 디샌딩 제일 마지막으로 설정 , 찍어서 중첩할수있음


    def __str__(self):  # 프린트를 해보거나 관리자 페이지에서 출력할때 씀
        return self.author.username + "" + self.created.strftime("%Y-%m-%d %H:%M:%S")  # 몇년 몇월 몇일 몇시 몇분 몇초에 생성되게끔 설정해주면됨


    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])