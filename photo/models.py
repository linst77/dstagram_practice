from django.db import models
from django.urls import reverse
# 장고의 기본 유저 모델
from django.contrib.auth.models import User

# Create your models here.

# foreignKey -  user 테이블에서 해당 유저(1)를 찾을수 있는 키
# PrimaryKey - user 테이블에 1 admin ***

class Photo( models.Model):
    author = models.ForeignKey( User, on_delete=models.CASCADE, related_name='user_photos')
    # on_delete-CASCADRE : 유저가 탈퇴할시 기존 데이터를 지운다. (PROTECT : 유저가 이미지를 다 지워야 탈퇴가 된다)
    # related_name =
    photo = models.ImageField( upload_to='photos/%Y/%m/%d', default="photos/no_image.png")
    # upload_to 파일이 들어가는 위치---함수를 만들어 customizing 가능하다
    # default = 이미지가 없을시 기본 이미지를 설정
    text = models.TextField()
    created = models.DateTimeField( auto_now_add=True)
    # auto_now_add = 데이터 베이스가 생길때
    updated = models.DateTimeField( auto_now=True)
    # auto_now = update, create등 갱신할때 생성


    # meta data
    # database를 쓸때 sort 및 다른 기능을 넣을수 있다.
    class Meta:
        ordering = ['-updated']

    def __str__ (self):
        # 사진계시중의 작성자를 불러온다 --- 생성된 날짜를 불러온다.
        return self.author.username + "" + self.created.strftime( "%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse( 'photo:photo_detail', args=[str(self.id)])
