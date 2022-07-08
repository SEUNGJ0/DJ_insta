from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Photo

# namespace로 사용되는 값. 템플릿에서 URL 템플릿 태그를 사용할 때 [app_name:URL패턴이름] 형태로 사용 
app_name = 'photo'

urlpatterns = [
    path('', photo_list, name = 'photo_list'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name = 'photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name = 'photo_update'),
    # DetailView는 urls.py에서 인라인 코드로 작성할 수 있다.
    path('detail/<int:pk>/', DetailView.as_view(model = Photo, template_name = 'Dj_Insta_photo/detail.html'), name='photo_detail'),
]