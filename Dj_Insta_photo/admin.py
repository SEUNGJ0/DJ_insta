from django.contrib import admin
from .models import Photo



# Admin 사이트에서 보이는 목록 화면을 커스터마이징 설정
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']  # 목록에 보일 필드를 설정
    raw_id_fields = ['author']                          # 
    list_filter = ['created', 'updated', 'author']       # 필터 기능을 사용할 필드를 선택
    search_fields = ['text', 'created']                 # 검색 기능을 사용할 필드를 선택
    ordering = ['-updated', '-created']                 # 정렬값 설정


admin.site.register(Photo, PhotoAdmin)