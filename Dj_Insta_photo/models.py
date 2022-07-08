from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Photo(models.Model):
    # ForeignKey를 사용하여  User 태아블과 관계를 생성
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()

    # 글 작성 일을 객체가 추가될 때 자동으로 설정
    created = models.DateTimeField(auto_now_add=True)
    # 글 수정 일을 수정될 때 자동으로 설정
    updated = models.DateTimeField(auto_now=True)

    # 해당 모델의 객체들의 정렬 기준을 설정 [ updated --> 내림차순 ]
    class Meta:
        ordering = ['-updated']

    # 해당 클레스 요청 시 반환값 설정  [ 작성자 이름과 글 작성일 반환 ]
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")
    
    # 객체의 상세 페이지의 주소를 반환
    def get_absolute_url(self):
        # reverse : URL 패턴이름을 가지고 해당 패턴을 찾아 주소로 만들어주는 함수
        return reverse('photo:photo_detail', args=[str(self.id)])
