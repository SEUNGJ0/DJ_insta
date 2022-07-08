"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Dj_Insta_photo.urls')),
    path('accounts/', include('Dj_Insta_accounts.urls'))
]

# static을 사용하여 MEDIA_URL에 해당하는 주소를 가진 요청에 대해서 MEDIA_ROOT에서 찾아서 응답하도록 설정
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
